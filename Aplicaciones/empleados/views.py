from django.shortcuts import render, redirect
from .models import Contacto, Empleado, TipoEmpleado
import datetime
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import redirect
from ..inicio.views import paginacionTablas

def home(request):
    empleados = Empleado().mostrarEmpleados()
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
    tipoEmpleados = TipoEmpleado.objects.all()

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
        fechaYHoraActual = datetime.datetime.now()
        fecha_alta_empleado = fechaYHoraActual.strftime("%Y-%m-%d")
        fecha_baja_empleado = request.POST.get('fecha_baja_empleado', None)
        id_tipo_empleado = request.POST.get('tipo_empleado')  # Recibe el tipo de empleado: "Facturador", "Asesor de Ventas", etc.
        
        # Datos de contacto
        tiposContacto = request.POST.getlist('tipo_contacto[]')
        contactos = request.POST.getlist('contacto[]')
        listaContactos = list(zip(tiposContacto, contactos))
        
        print("Datos recibidos en la vista:")
        print("Nombre:", nombre_persona)
        print("Apellido:", apellido_persona)
        print("CUIT:", cuitl_persona)
        print("Dirección:", direccion_persona)
        print("Tipo de empleado:", id_tipo_empleado)
        print("Fecha de alta empleado:", fecha_alta_empleado)
        print("Fecha de baja empleado:", fecha_baja_empleado)
        print("Lista de contactos:", listaContactos)

        # Verificar si el empleado ya existe
        empleado = Empleado()
        if empleado.empleadoExiste(cuitl_persona):
            messages.error(request, 'El empleado ya existe.')
        else:
            # Agregar nuevo empleado
            id_empleado = empleado.agregarEmpleado(
                nombre_persona, apellido_persona, cuitl_persona,
                direccion_persona, fecha_alta_empleado, fecha_baja_empleado,
                id_tipo_empleado, listaContactos
            )
            
            if id_empleado:
                messages.success(request, 'El empleado se agregó correctamente.')
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
        id_tipo_empleado = request.POST.get('tipo_empleado_editar')

        # Recopilación de los contactos existentes y nuevos
        contactos_data = []
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

        # Agregar print para ver los contactos que están llegando
        print("Datos de contacto editados o nuevos:", contactos_data)

        # Llamada al método para actualizar el empleado
        Empleado().editarEmpleado(
            id_empleado,
            nombre_persona,
            apellido_persona,
            cuitl_persona,
            direccion_persona,
            id_tipo_empleado,
            contactos_data  # Pasa todos los contactos para su procesamiento
        )

    return redirect('empleados:home')


def eliminarEmpleado(request, id_empleado):
    Empleado().eliminarEmpleado(id_empleado)
    return redirect('empleados:home')


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
 