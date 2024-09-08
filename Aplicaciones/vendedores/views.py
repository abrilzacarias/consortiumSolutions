from django.shortcuts import render, redirect
from .models import Empleado, Contacto
import datetime
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import redirect

def home(request):
    vendedores = Empleado().mostrarVendedor()

    for vendedor in vendedores:
        contactos = Contacto.objects.filter(id_persona=vendedor['id_persona'])
        vendedor['contactos'] = [
            {
                'id_contacto': contacto.id_contacto,
                'tipo_contacto': contacto.id_tipo_contacto.descripcion_tipo_contacto,
                'tipo_contacto_id': contacto.id_tipo_contacto.id_tipo_contacto,
                'descripcion_contacto': contacto.descripcion_contacto
            }
            for contacto in contactos
        ]
    return render(request, 'vendedoresviews.html', {'vendedores': vendedores})


def agregarVendedor(request):
    if request.method == 'POST':
        nombre_persona = request.POST.get('nombre_persona')
        apellido_persona = request.POST.get('apellido_persona')
        cuitl_persona = request.POST.get('cuitl_persona')
        direccion_persona = request.POST.get('direccion_persona')
        fechaYHoraActual = datetime.datetime.now()
        fecha_alta_vendedor = fechaYHoraActual.strftime("%Y-%m-%d")
        fecha_baja_vendedor = request.POST.get('fecha_baja_vendedor', None)
        tiposContacto = request.POST.getlist('tipo_contacto[]')
        contactos = request.POST.getlist('contacto[]')

        listaContactos = list(zip(tiposContacto, contactos))
        
        print("Datos recibidos en la vista:")
        print("Nombre:", nombre_persona)
        print("Apellido:", apellido_persona)
        print("CUIT:", cuitl_persona)
        print("Dirección:", direccion_persona)
        print("Fecha de alta vendedor:", fecha_alta_vendedor)
        print("Fecha de baja vendedor:", fecha_baja_vendedor)
        print("Lista de contactos:", listaContactos)

        vendedor = Empleado()

        if vendedor.vendedorExiste(cuitl_persona):
            messages.error(request, 'El vendedor ya existe.')
        else: 

            id_vendedor = vendedor.agregarVendedor(
                nombre_persona, apellido_persona, cuitl_persona,
                direccion_persona, fecha_alta_vendedor, fecha_baja_vendedor,
                listaContactos
            )
            if id_vendedor:
                messages.success(request, 'El vendedor se agregó correctamente.')
                return redirect('/vendedores/')  
            else:
                messages.error(request, 'El vendedor se agregó correctamente.')
    return redirect('/vendedores/')

def editarVendedor(request, id_vendedor):
    if request.method == 'POST':
        nombre_persona = request.POST.get('nombre_persona_editar')
        apellido_persona = request.POST.get('apellido_persona_editar')
        cuitl_persona = request.POST.get('cuitl_persona_editar')
        direccion_persona = request.POST.get('direccion_persona')

        contactos_data = []
        for key, value in request.POST.items():
            if key.startswith('tipo_contacto_'):
                contacto_id = key.split('_')[-1]
                tipo_contacto_id = value
                descripcion_contacto = request.POST.get(f'contacto_{contacto_id}')
                contactos_data.append({
                    'id_contacto': contacto_id,
                    'tipo_contacto_id': tipo_contacto_id,
                    'descripcion_contacto': descripcion_contacto
                })

            elif key.startswith('nuevo_contacto_tipo_'):  
                tipo_contacto_id = value.split('_')[-1]
                unique_id = key.split('_')[-1]  
                descripcion_contacto = request.POST.get(f'nuevo_contacto_descripcion_{unique_id}')
                contactos_data.append({
                'id_contacto': None,
                'tipo_contacto_id': tipo_contacto_id,
                'descripcion_contacto': descripcion_contacto
                })
        
        
        print(contactos_data)

        Empleado().editarVendedor(id_vendedor,nombre_persona,apellido_persona,cuitl_persona,direccion_persona, contactos_data)
    return redirect('vendedores:home')  # Redirige al usuario a la página principal de vendedores

def eliminarVendedor(request, id_vendedor):
    Empleado().eliminarVendedor(id_vendedor)
    return redirect('vendedores:home')


def eliminarContacto(request, id_contacto):
  if request.method == 'DELETE':
    try:
      contacto = Contacto.objects.get(pk=id_contacto)
      contacto.delete()
      return JsonResponse({'message': 'Contacto eliminado con éxito.'})
    except Contacto.DoesNotExist:
      return JsonResponse({'error': 'El contacto con ID especificado no existe.'}, status=404)
    except Exception as e:
      return JsonResponse({'error': 'Error al eliminar el contacto.'}, status=500)
  else:
    return HttpResponse(status=405) 