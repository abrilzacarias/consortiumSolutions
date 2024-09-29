from django.shortcuts import render, redirect
from .models import Clientes, Contacto, Edificio
from ..empleados.models import Empleado
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime
from ..inicio.views import paginacionTablas

empleado = Empleado()
clientes = Clientes()

@login_required
@permission_required('inicio.view_cliente', login_url='', raise_exception=True)
def listarClientes(request):
    es_vendedor = request.user.groups.filter(name='empleados').exists()  # Ajusta según tu lógica para identificar vendedores
    resultados = clientes.listarClientes()
    empleados = empleado.mostrarEmpleados()
    resultados_modificados = []
    # Obtén el ID del vendedor si es vendedor
    if es_vendedor:
        try:
            vendedorUsuario = Empleado.objects.get(id_usuario=request.user.id_usuario)
            id_vendedor_user = vendedorUsuario.id_vendedor
            print("El vendedor existe.")
        except Empleado.DoesNotExist:
            pass
    # Filtra clientes si es un vendedor
    for cliente in resultados:
        if len(cliente) > 10:
            id_edificios = cliente[12].split(', ') if cliente[12] else []
            nombre_edificios = cliente[13].split(', ') if cliente[13] else []
            direccion_edificios = cliente[14].split(', ') if cliente[14] else []
            cuit_edificios = cliente[15].split(', ') if cliente[15] else []
            tipo_edificios = cliente[16].split(', ') if cliente[16] else []
            fecha_baja_edificios = cliente[25].split(', ') if cliente[25] else []
        else:
            id_edificios = []
            nombre_edificios = []
            direccion_edificios = []
            cuit_edificios = []
            tipo_edificios = []
            fecha_baja_edificios = []

        edificios = []
        for i in range(len(nombre_edificios)):
            edificio = {
                'id_edificio': id_edificios[i] if i < len(id_edificios) else '',
                'nombre_edificio': nombre_edificios[i] if i < len(nombre_edificios) else '',
                'direccion_edificio': direccion_edificios[i] if i < len(direccion_edificios) else '',
                'cuit_edificio': cuit_edificios[i] if i < len(cuit_edificios) else '',
                'tipo_edificio': tipo_edificios[i] if i < len(tipo_edificios) else '', 
                'fecha_baja_edificio': fecha_baja_edificios[i] if i < len(fecha_baja_edificios) else ''
            }
            edificios.append(edificio)
        
        nombre_vendedor_asignado = cliente[18] if len(cliente) > 18 else ''

        ids_observaciones = cliente[21].split(', ') if cliente[21] else []
        descripciones_observaciones = cliente[22].split('|') if cliente[22] else []
        fechas_observaciones = cliente[23].split(', ') if cliente[23] else []
        horas_observaciones  = cliente[24].split(', ') if cliente[24] else []

        
        
        observaciones = []
        for i in range(len(ids_observaciones)):
            observacion = {
                'id_observacion': ids_observaciones[i] if i < len(ids_observaciones) else '',
                'descripcion_observacion': descripciones_observaciones[i] if i < len(descripciones_observaciones) else '',
                'fecha_observacion': fechas_observaciones[i] if i < len(fechas_observaciones) else '',
                'hora_observacion': horas_observaciones[i] if i < len(horas_observaciones) else ''
            }
            observaciones.append(observacion)
        
        idpersona = clientes.obtenerIdPersona(cliente[0])
        cliente_modificado = {
            'id_cliente': cliente[0],
            'nombre_cliente': cliente[1] if len(cliente) > 1 else '',
            'apellido_cliente': cliente[2] if len(cliente) > 2 else '',
            'cuit_cliente': cliente[3] if len(cliente) > 3 else '',
            'direccion_cliente': cliente[4] if len(cliente) > 4 else '',
            'clave_cliente': cliente[5] if len(cliente) > 5 else '',
            'tipo_cliente': cliente[6] if len(cliente) > 6 else '',
            'fecha_baja_cliente': cliente[7] if len(cliente) > 7 else '',
            'matricula_cliente': cliente[8] if len(cliente) > 9 else '',
            'fecha_vencimiento': cliente[9] if len(cliente) > 10 else '',
            'contacto_cliente': cliente[10] if len(cliente) > 11 else '',
            'tipo_contacto': cliente[11] if len(cliente) > 12 else '',
            'edificios': edificios,  
            'vendedor_asignado': nombre_vendedor_asignado,  
            'id_vendedor_asignado': cliente[17] if len(cliente) > 17 else '',
            'observaciones': observaciones, 
            'id_persona': idpersona
        }
        
        contactos = Contacto.objects.filter(id_persona=cliente_modificado['id_persona'])
        
        cliente_modificado['contactos'] = [
            {
                'id_contacto': contacto.id_contacto,
                'tipo_contacto': contacto.id_tipo_contacto.descripcion_tipo_contacto,
                'tipo_contacto_id': contacto.id_tipo_contacto.id_tipo_contacto,
                'descripcion_contacto': contacto.descripcion_contacto
            }
            for contacto in contactos
        ]

        resultados_modificados.append(cliente_modificado)

    if es_vendedor:
        resultados_modificados = [cliente for cliente in resultados_modificados if cliente['id_vendedor_asignado'] == id_vendedor_user]

    context = paginacionTablas(request, resultados_modificados, 'resultados')
    context['empleados'] = empleados
        
    return render(request, 'clientesviews.html', context)

def agregarCliente(request):
    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre_cliente')
        apellido_cliente = request.POST.get('apellido_cliente')
        cuitl_cliente = request.POST.get('cuitl_cliente')
        direccion_cliente = request.POST.get('direccion_cliente')
        clave_afgip_cliente = request.POST.get('clave_afgip_cliente')
        tipo_cliente = int(request.POST.get('tipo_cliente'))  # Convertir el valor del dropdown a entero
        matricula_cliente = request.POST.get('matricula_cliente')
        vencimiento_matricula = request.POST.get('vencimiento_matricula')
        vendedor_asignado = request.POST.get('vendedor_asignado')

        tipos_contacto = request.POST.getlist('tipo_contacto[]')
        contactos = request.POST.getlist('contacto[]')
        

        # Crear una lista de contactos como tuplas (tipo_contacto, contacto)
        lista_contactos = list(zip(tipos_contacto, contactos))
        
        # Agregar el cliente y obtener el id_cliente
        id_cliente = clientes.agregarCliente(nombre_cliente, apellido_cliente, cuitl_cliente, direccion_cliente, clave_afgip_cliente, tipo_cliente, matricula_cliente, vencimiento_matricula, lista_contactos, vendedor_asignado)
       
        if id_cliente:
            
            # Ahora que tienes el id_cliente, agrega la designación del vendedor si hay uno asignado
            if vendedor_asignado:
                if clientes.agregarDesignacionVendedor(vendedor_asignado, id_cliente):
                    messages.success(request, 'El cliente y la designación se agregaron correctamente.')
                else:
                    messages.error(request, 'El cliente se agregó, pero hubo un error al agregar la designación del vendedor.')
            else:
                messages.success(request, 'El cliente se agregó correctamente, sin designación de vendedor.')
                
            return redirect('/clientes/')
        else:
            messages.error(request, 'Hubo un error al agregar el cliente.')
            return redirect('/clientes/')
    else:
        empleados = empleado.mostrarEmpleados()
        return render(request, 'clientesviews.html', {'empleados': empleados})


def editarCliente(request, id_cliente):
    clientes = Clientes()
    
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre_persona = request.POST.get('nombre_persona')
        apellido_persona = request.POST.get('apellido_persona')
        cuitl_persona = request.POST.get('cuitl_persona')
        direccion_persona = request.POST.get('direccion_persona')
        clave_afgip_cliente = request.POST.get('clave_afgip_cliente')
        tipo_cliente = request.POST.get('tipo_cliente')
        matricula_cliente = request.POST.get('matricula_cliente')
        vencimiento_matricula = request.POST.get('vencimiento_matricula')
        vendedor_asignado = request.POST.get('vendedor_asignado')  

        print(f"ID Cliente recibido: {id_cliente}")  # Verifica el ID del cliente
        
        print(f"Vendedor asignado recibido: {vendedor_asignado}")
        
        
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

        
        # Verificar que el cliente existe
        cliente_actual = clientes.obtenerClientePorId(id_cliente)
        if not cliente_actual:
            return HttpResponse("El cliente no existe")

        vendedor_actual = cliente_actual.get('id_vendedor_asignado')

        # Manejar la designación de vendedores
        if vendedor_asignado:
            # Verifica si el vendedor asignado es diferente al actual
            if vendedor_actual != vendedor_asignado:
                if vendedor_actual:
                    # Eliminar la designación del vendedor actual
                    if not clientes.eliminarDesignacionVendedor(id_cliente, vendedor_actual):
                        return HttpResponse("Hubo un error al eliminar la designación del vendedor actual.")
                # Asignar el nuevo vendedor
                if not clientes.agregarDesignacionVendedor(vendedor_asignado, id_cliente):
                    return HttpResponse("Hubo un error al asignar el nuevo vendedor.")
        else:
            # Si no se ha asignado un vendedor, elimina la designación actual
            if vendedor_actual:
                if not clientes.eliminarDesignacionVendedor(id_cliente, vendedor_actual):
                    return HttpResponse("Hubo un error al eliminar la designación del vendedor actual.")

        # Llamar a la función editarCliente para realizar la actualización
        actualizado = clientes.editarCliente(
            id_cliente, 
            nombre_persona, 
            apellido_persona, 
            cuitl_persona, 
            direccion_persona, 
            clave_afgip_cliente, 
            tipo_cliente, 
            matricula_cliente, 
            vencimiento_matricula, 
            contactos_data
        )

        if not actualizado:
            return HttpResponse("Hubo un error al editar el cliente.")
        
        return redirect('/clientes/')
    
    else:
        # Obtener los datos del cliente y los empleados para mostrar en el formulario
        cliente = clientes.obtenerClientePorId(id_cliente)
        empleados = Empleado().mostrarEmpleados()
        return render(request, 'clientesviews.html', {'cliente': cliente, 'empleados': empleados})



def eliminarCliente(request, id_cliente):
    clientes.eliminarCliente(id_cliente)
    return redirect('/clientes/') 

def agregarEdificio(request, id_cliente):
    if request.method == 'POST':
        nombre_edificio = request.POST.get('nombre_edificio')
        direccion_edificio = request.POST.get('direccion_edificio')
        cuit_edificio = request.POST.get('cuit_edificio')
        tipo_edificio = request.POST.get('tipo_edificio')

        tipo_edificio = int(tipo_edificio)


        clientes.agregarEdificio(nombre_edificio, direccion_edificio, cuit_edificio, tipo_edificio, id_cliente)

    return redirect('/clientes/')

def agregarDesignacionVendedor(request, id_cliente):
    if request.method == 'POST':
        vendedor_asignado = request.POST.get('vendedor_asignado')  
        
        clientes = Clientes()
        
        # Llama al método agregarDesignacionVendedor con los IDs del vendedor y el cliente
        if clientes.agregarDesignacionVendedor(vendedor_asignado, id_cliente):
            # Si la inserción fue exitosa, redirige a una página de éxito
            return redirect('/clientes/')
        else:
            return HttpResponse("Hubo un error al agregar la designación de vendedor.")
    else:
        return HttpResponseNotAllowed(['POST'])

def agregarObservacionCliente(request, id_cliente):
    if request.method == 'POST':
        descripcion_observacion = request.POST.get('descripcion_observacion')
        clientes.agregarObservacion(id_cliente, descripcion_observacion)
    return redirect('/clientes/')


def eliminarContactoCliente(request, id_contacto):
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
    

def editarEdificio(request, id_edificio):
    clientes = Clientes()
    if request.method == 'POST':
        nombre_edificio = request.POST.get('nombre_edificio')
        direccion_edificio = request.POST.get('direccion_edificio')
        cuit_edificio = request.POST.get('cuit_edificio')
        tipo_edificio = request.POST.get('tipo_edificio')
        actualizado = clientes.editarEdificio(
            id_edificio, nombre_edificio, direccion_edificio, cuit_edificio, tipo_edificio
        )
        if not actualizado:
            return HttpResponse("Hubo un error al editar el cliente.")
        return redirect('/clientes/')
    else:
        return redirect('/clientes/')
    
def eliminarEdificio(request, id_edificio):

    Clientes().eliminarEdificio(id_edificio)
    return redirect('/clientes/') 



