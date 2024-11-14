from django.shortcuts import render, redirect
from .models import Contacto, Empleado, TipoEmpleado
import datetime
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import redirect
from ..inicio.views import paginacionTablas
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
current_datetime = timezone.localtime(timezone.now())

@login_required
def home(request):
    query = request.GET.get('busquedaEmpleado', '')  # Toma el parámetro 'q' del GET
    
    # Llamar a `mostrarEmpleados` para obtener todos los empleados de una vez
    empleados = Empleado().mostrarEmpleados()
    
    if query:
        query = query.lower()
        empleados = [
            empleado for empleado in empleados
            if empleado['nombre_persona'].lower().startswith(query) or
                empleado['apellido_persona'].lower().startswith(query) or
                empleado['cuitl_persona'].startswith(query)
            ]

    for empleado in empleados:
        contactos = Contacto.objects.filter(id_persona=empleado['id_persona'])
        empleado['contactos'] = [
            {
                'id_contacto': contacto.id_contacto,
                'tipo_contacto': contacto.id_tipo_contacto.descripcion_tipo_contacto,
                'tipo_contacto_id': contacto.id_tipo_contacto.id_tipo_contacto,
                'descripcion_contacto': contacto.descripcion_contacto
            }
            for contacto in contactos
        ]
    
    # Obtener los tipos de empleados solo una vez
    tipoEmpleados = TipoEmpleado.objects.all()

    # Paginación y contexto
    context = paginacionTablas(request, empleados, 'empleados')
    context['tipo_empleados'] = tipoEmpleados
    
    return render(request, 'empleadoViews.html', context)


def agregarEmpleado(request):
    if request.method == 'POST':
        # Datos de persona
        nombre_persona = request.POST.get('nombre_persona')
        apellido_persona = request.POST.get('apellido_persona')
        cuitl_persona = request.POST.get('cuitl_persona')
        direccion_persona = request.POST.get('direccion_persona')
        
        # Datos de empleado
        fecha_alta_empleado = current_datetime
        fecha_baja_empleado = request.POST.get('fecha_baja_empleado', None)
        id_tipo_empleado_lista = request.POST.getlist('tipo_empleado')  # Recibe una lista de tipos de empleado
        correo_electronico = request.POST.get('correo_electronico') #se usa para crear el USER
        
        # Datos de contacto
        tiposContacto = request.POST.getlist('tipo_contacto[]')
        contactos = request.POST.getlist('contacto[]')
        listaContactos = list(zip(tiposContacto, contactos))

        # Verificar si el empleado ya existe
        empleado = Empleado()
        if empleado.empleadoExiste(cuitl_persona):
            messages.error(request, 'El empleado ya existe.')
        else:
            # Agregar nuevo empleado
            id_empleado = empleado.agregarEmpleado(
                nombre_persona, apellido_persona, cuitl_persona,
                direccion_persona, fecha_alta_empleado, fecha_baja_empleado,
                id_tipo_empleado_lista, listaContactos, correo_electronico
            )
            if id_empleado:
                messages.success(request, 'El empleado se agregó correctamente y se enviaron las credenciales de acceso al correo electrónico indicado.')
                return redirect('/empleados/')  # Redirigir a la lista de empleados
            else:
                messages.error(request, 'Error al agregar el empleado.')
    return redirect('/empleados/')

def editarEmpleado(request, id_empleado):
    if request.method == 'POST':
        # Datos de la persona
        nombre_persona = request.POST.get('nombre_persona_editar')
        apellido_persona = request.POST.get('apellido_persona_editar')
        cuitl_persona = request.POST.get('cuitl_persona_editar')
        direccion_persona = request.POST.get('direccion_persona_editar')
        id_tipo_empleado_lista = request.POST.getlist('tipo_empleado_editar')

        contactos_data = []
        correo_id = request.POST.get('id_contacto_correo')
        correo_descripcion = request.POST.get('descripcion_contacto_correo')
        if correo_descripcion:
            contactos_data.append({
                'id_contacto': correo_id,
                'tipo_contacto_id': 1,  # Asumiendo que 1 es para correo
                'descripcion_contacto': correo_descripcion
            })

        for key, value in request.POST.items():
            if key.startswith('tipo_contacto_'):
                contacto_id = key.split('_')[-1]
                tipo_contacto_id = value
                descripcion_contacto = request.POST.get(f'contacto_{contacto_id}')
                
                # Solo agregamos si la descripción no está vacía
                if descripcion_contacto:
                    contactos_data.append({
                        'id_contacto': contacto_id,  # Mantén el ID si es un contacto existente
                        'tipo_contacto_id': tipo_contacto_id,
                        'descripcion_contacto': descripcion_contacto
                    })
            elif key.startswith('nuevo_contacto_tipo_'):
                unique_id = key.split('_')[-1]
                tipo_contacto_id = value
                descripcion_contacto = request.POST.get(f'nuevo_contacto_descripcion_{unique_id}')
                
                if descripcion_contacto:
                    contactos_data.append({
                        'id_contacto': None,  # Nuevo contacto, sin ID
                        'tipo_contacto_id': tipo_contacto_id,
                        'descripcion_contacto': descripcion_contacto
                    })

        # Llamada al método para actualizar el empleado
        actualizado = Empleado().editarEmpleado(
            id_empleado,
            nombre_persona,
            apellido_persona,
            cuitl_persona,
            direccion_persona,
            id_tipo_empleado_lista,
            contactos_data  # Pasa todos los contactos para su procesamiento
        )

        if actualizado:
            messages.success(request, 'El empleado se editó correctamente.')
        else:
            messages.error(request, 'Hubo un error al editar el empleado.')

        return redirect('empleados:home')

    else:
        messages.error(request, 'Método no permitido.')
        return redirect('empleados:home')


from django.contrib import messages

def eliminarEmpleado(request, id_empleado):
    empleado = Empleado()
    eliminado = empleado.eliminarEmpleado(id_empleado)  # Se asume que devuelve True si se elimina correctamente

    if eliminado:
        messages.success(request, 'El empleado se eliminó correctamente.')
    else:
        messages.error(request, 'Hubo un error al intentar eliminar el empleado.')

    return redirect('/empleados/')



def eliminarContactoEmpleado(request, id_contacto):
    if request.method == 'DELETE':
        try:
            contacto = Contacto.objects.get(pk=id_contacto)
            contacto.delete()
            return JsonResponse({'message': 'Contacto eliminado con éxito.'})
        except Contacto.DoesNotExist:
            return JsonResponse({'error': 'El contacto con ID especificado no existe.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Error al eliminar el contacto: {str(e)}'}, status=500)
    else:
        return HttpResponse(status=405)
 
