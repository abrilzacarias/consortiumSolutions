from django.shortcuts import render, redirect
from .models import Clientes, Contacto
from ..vendedores.models import Vendedor
from django.http import HttpResponse, HttpResponseNotAllowed
from django.utils import timezone
from django.contrib import messages

vendedor = Vendedor()
clientes = Clientes()

def listarClientes(request):
    resultados = clientes.listarClientes()
    vendedores = vendedor.mostrarVendedor()
    
    resultados_modificados = []
    
    for cliente in resultados:
        if len(cliente) > 10:
            nombre_edificios = cliente[12].split(', ') if cliente[12] else []
            direccion_edificios = cliente[13].split(', ') if cliente[13] else []
            cuit_edificios = cliente[14].split(', ') if cliente[14] else []
            tipo_edificios = cliente[15].split(', ') if cliente[15] else []
        else:
            nombre_edificios = []
            direccion_edificios = []
            cuit_edificios = []
            tipo_edificios = []

        edificios = []
        for i in range(len(nombre_edificios)):
            edificio = {
                'nombre_edificio': nombre_edificios[i] if i < len(nombre_edificios) else '',
                'direccion_edificio': direccion_edificios[i] if i < len(direccion_edificios) else '',
                'cuit_edificio': cuit_edificios[i] if i < len(cuit_edificios) else '',
                'tipo_edificio': tipo_edificios[i] if i < len(tipo_edificios) else ''
            }
            edificios.append(edificio)
        
        id_vendedor_asignado = cliente[17] if len(cliente) > 17 else ''
        
        ids_observaciones = cliente[18].split(', ') if cliente[18] else []
        descripciones_observaciones = cliente[19].split('|') if cliente[19] else []
        fechas_observaciones = cliente[20].split(', ') if cliente[20] else []
        
        observaciones = []
        for i in range(len(ids_observaciones)):
            observacion = {
                'id_observacion': ids_observaciones[i] if i < len(ids_observaciones) else '',
                'descripcion_observacion': descripciones_observaciones[i] if i < len(descripciones_observaciones) else '',
                'fecha_hora_observacion': fechas_observaciones[i] if i < len(fechas_observaciones) else ''
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
            'vendedor_asignado': cliente[16] if len(cliente) > 16 else '',  
            'id_vendedor_asignado': id_vendedor_asignado,  
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
        
    return render(request, 'clientesviews.html', {'resultados': resultados_modificados, 'vendedores': vendedores})


def agregarCliente(request):
    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre_cliente')
        apellido_cliente = request.POST.get('apellido_cliente')
        cuitl_cliente = request.POST.get('cuitl_cliente')
        direccion_cliente = request.POST.get('direccion_cliente')
        clave_afgip_cliente = request.POST.get('clave_afgip_cliente')
        tipo_cliente = request.POST.get('tipo_cliente')  # Convertir el valor del dropdown a un booleano
        matricula_cliente = request.POST.get('matricula_cliente')  
        vencimiento_matricula = request.POST.get('vencimiento_matricula')
        vendedor_asignado = request.POST.get('vendedor_asignado')
        print(f'LLEGA VENDEDOR A VIEWSSSSSSSS {vendedor_asignado}')
        tipo_cliente = int(tipo_cliente)

        tipos_contacto = request.POST.getlist('tipo_contacto[]')
        contactos = request.POST.getlist('contacto[]')
        
        # Crear una lista de contactos como tuplas (tipo_contacto, contacto)
        lista_contactos = list(zip(tipos_contacto, contactos))
        id_cliente = clientes.agregarCliente(nombre_cliente, apellido_cliente, cuitl_cliente, direccion_cliente, clave_afgip_cliente, tipo_cliente, matricula_cliente, vencimiento_matricula, lista_contactos, vendedor_asignado)
        if id_cliente:
            messages.success(request, 'El cliente se agregó correctamente.')
            return redirect('/clientes/')
        else:
            messages.error(request, 'Hubo un error al agregar el cliente.')
            return redirect('/clientes/')
    else:
        vendedores = vendedor.mostrarVendedor()
        return render(request, 'agregarcliente.html', {'vendedores': vendedores})

def editarCliente(request, id_cliente):
    if request.method == 'POST':
        nombre_persona = request.POST.get('nombre_persona')
        apellido_persona = request.POST.get('apellido_persona')
        cuitl_persona = request.POST.get('cuitl_persona')
        direccion_persona = request.POST.get('direccion_persona')
        clave_afgip_cliente = request.POST.get('clave_afgip_cliente')
        tipo_cliente = request.POST.get('tipo_cliente')
        matricula_cliente = request.POST.get('matricula_cliente')
        vencimiento_matricula = request.POST.get('vencimiento_matricula')
        vendedor_asignado = request.POST.get('vendedor_asignado')  
        print(f'vendedor ASIGNADO {vendedor_asignado}')

        tipo_cliente = int(tipo_cliente)

        # Procesar los datos de los contactos
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

        cliente_actual = clientes.obtenerClientePorId(id_cliente)
        vendedor_actual = cliente_actual.get('id_vendedor_asignado') if cliente_actual else None
        
        if vendedor_asignado == '':
            if vendedor_actual:
                if not clientes.eliminarDesignacionVendedor(id_cliente, vendedor_actual):
                    return HttpResponse("Hubo un error al eliminar la designación del vendedor actual.")
            else:
                print("No hay vendedor asignado y no se asignó uno nuevo.")
        elif vendedor_actual != vendedor_asignado:
            if vendedor_actual:
                print(f'vendedor actual {vendedor_actual}')
                # Cambiar el vendedor asignado
                if not clientes.eliminarDesignacionVendedor(id_cliente, vendedor_actual):
                    return HttpResponse("Hubo un error al eliminar la designación del vendedor actual.")
            if not clientes.agregarDesignacionVendedor(vendedor_asignado, id_cliente):
                return HttpResponse("Hubo un error al agregar la nueva designación de vendedor.")

        # Llamar a la función editarCliente del modelo
        if not clientes.editarCliente(id_cliente, nombre_persona, apellido_persona, cuitl_persona, direccion_persona, clave_afgip_cliente, tipo_cliente, matricula_cliente, vencimiento_matricula, contactos_data):
            return HttpResponse("Hubo un error al editar el cliente.")

        return redirect('/clientes/')
    else:
        cliente = clientes.obtenerClientePorId(id_cliente)
        print(cliente)
        
        vendedores = vendedor.mostrarVendedor()
        return render(request, 'editarcliente.html', {'cliente': cliente, 'vendedores': vendedores})



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
        id_vendedor = request.POST.get('vendedor')
        
        clientes = Clientes()
        
        # Llama al método agregarDesignacionVendedor con los IDs del vendedor y el cliente
        if clientes.agregarDesignacionVendedor(id_vendedor, id_cliente):
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




