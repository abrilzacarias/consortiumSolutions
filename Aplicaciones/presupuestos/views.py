from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Presupuesto, DetallePresupuesto, Observacion
from django.contrib import messages
from ..clientes.models import Cliente, Edificio
from ..empleados.models import Empleado
from ..servicios.models import CategoriaServicio
from ..inicio.views import paginacionTablas
from django.contrib.auth.decorators import login_required, permission_required

#TODO  @permission_required('inicio.view_detalleventa', login_url='', raise_exception=True) AGREGAR A TODAS PERO PRIMERO HAY QUE CONFIGURAR ADMIN BIEN
@login_required
@permission_required('inicio.view_cliente', login_url='', raise_exception=True)
def home(request):
    es_vendedor = request.user.groups.filter(name='Vendedor').exists()
    presupuestos = Presupuesto.listarPresupuestos()
    print(presupuestos)
    if es_vendedor:
        try:
            vendedorUsuario = Empleado.objects.get(id_usuario=request.user.id_usuario)
            id_vendedor_user = vendedorUsuario.id_empleado
        except Empleado.DoesNotExist:
            pass
    
    if es_vendedor:
        print("El vendedor existe.")
        presupuestos = [p for p in presupuestos if p['id_empleado'] == id_vendedor_user]

    context = paginacionTablas(request, presupuestos, 'presupuestos')
    return render(request, 'listarPresupuestos.html', context)

def detalle_presupuesto(request, id_presupuesto): 
    detalle_presupuesto = [detalle for detalle in DetallePresupuesto.listarDetallePresupuesto() if detalle['id_presupuesto'] == id_presupuesto]
    print(detalle_presupuesto)
    return JsonResponse(detalle_presupuesto, safe=False)

@login_required
@permission_required('inicio.view_cliente', login_url='', raise_exception=True)
def agregarPresupuesto(request):
    if request.method == 'POST':
        #campos de presupuesto
        monto_total_presupuesto = request.POST.get('totalCost')
        id_edificio = request.POST.get('edificio_asignado')
        id_empleado = request.POST.get('vendedor_asignado')

        #campos de detalle de presupuesto
        lista_cantidad_detalle_presupuesto = request.POST.getlist('cantidades[]')
        #lista_precio_unitario_detalle_presupuesto = request.POST.getlist('precios_unitarios[]')
        costos_extra = request.POST.getlist('costos_extra[]')
        lista_precio_total_detalle_presupuesto = request.POST.getlist('subtotales[]')
        lista_id_servicio = request.POST.getlist('servicios[]')
        
        # Crear una lista de detalles
        #PRECIO UNITARIO ES EL COSTO EXTRA
        lista_detalles = [
            {
                'id_servicio': id_servicio,
                'cantidad': cantidad,
                'costo_extra_presupuesto': costos_extra,
                'precio_total': precio_total
            }
            for id_servicio, cantidad, costos_extra, precio_total in zip(
                lista_id_servicio,
                lista_cantidad_detalle_presupuesto,
                costos_extra,
                lista_precio_total_detalle_presupuesto
            )
        ]
        #print(lista_detalles)
        id_presupuesto = Presupuesto.insertarPresupuesto(monto_total_presupuesto, id_edificio, id_empleado, lista_detalles)
        if id_presupuesto:
           messages.success(request, 'El presupuesto se agregó correctamente.')
           return redirect('/presupuestos/')
        else:
           messages.error(request, 'Hubo un error al agregar el presupuesto.')
        return redirect('/presupuestos/')
    else:
        presupuestos = Presupuesto.listarPresupuestos()
        return render(request, {'presupuestos': presupuestos})
    

@login_required
@permission_required('inicio.view_cliente', login_url='', raise_exception=True)
def mostrar_vendedores(request, method='GET'):
    user = request.user
    print()
    
    if user.is_superuser:
        # Si es superusuario, mostramos todos los vendedores
        vendedores = Presupuesto.filtrarVendedores()
    else:
        # Si es un vendedor, solo mostramos el registro del vendedor asociado
        try:
            user = user.id_usuario
            vendedor = Empleado.objects.get(id_usuario=user)
            vendedores = [(vendedor.id_empleado, vendedor.id_persona.nombre_persona, vendedor.id_persona.apellido_persona)]  # Convertimos a lista para mantener formato JSON consistente
            print(f'Vendedor: {vendedores}')
        except Empleado.DoesNotExist:
            return JsonResponse({'error': 'No se encontró el vendedor asociado al usuario'}, status=404)
        
    vendedores_list = [
                {
                    'id_empleado': vendedor[0],
                    'id_persona__nombre_persona': vendedor[1],
                    'id_persona__apellido_persona': vendedor[2]
                }
                for vendedor in vendedores
                                ]
    
    return JsonResponse(vendedores_list, safe=False)

@login_required
@permission_required('inicio.view_cliente', login_url='', raise_exception=True)
def mostrar_clientes(request, method='GET'):
    servicios = list(
        Cliente.objects.select_related('id_persona')
        .filter(fecha_baja_cliente__isnull=True)
        .values('id_cliente', 'id_persona__nombre_persona', 'id_persona__apellido_persona')  # Corrige aquí
    )
    
    return JsonResponse(servicios, safe=False)


@login_required
@permission_required('inicio.view_presupuesto', login_url='', raise_exception=True)
def mostrar_edificios(request, id_cliente):
    edificios = list(Edificio.objects.filter(id_cliente=id_cliente).values('id_edificio', 'nombre_edificio'))
    
    return JsonResponse(edificios, safe=False)

@login_required
@permission_required('inicio.view_cliente', login_url='', raise_exception=True)
def obtener_servicios(request):
    categorias = CategoriaServicio.objects.prefetch_related('servicios').all()
    
    response_data = []
    
    for categoria in categorias:
        servicios = categoria.servicios.all()
        servicios_data = [
            {
                'id': servicio.id_servicio,
                'nombre': servicio.nombre_servicio,
                'precio': float(servicio.precio_base_servicio)
            }
            for servicio in servicios
        ]
        response_data.append({
            'categoria': categoria.nombre_categoria_servicio,
            'servicios': servicios_data
        })

    return JsonResponse(response_data, safe=False)

@login_required
@permission_required('inicio.view_cliente', login_url='', raise_exception=True)
def eliminarPresupuesto(request, id_presupuesto):
    if request.method == 'POST':
        presupuesto = get_object_or_404(Presupuesto, id_presupuesto=id_presupuesto)
        
        # Verifica si el presupuesto está referenciado en MensajePresupuesto
        detalles = DetallePresupuesto.objects.filter(id_presupuesto=presupuesto.id_presupuesto)
        #print(detalles)
        if detalles.exists():
             detalles.delete()
             presupuesto.delete()
             messages.success(request, "Presupuesto y detalles eliminados con éxito.")
        else:
            presupuesto.delete()
            messages.success(request, "Presupuesto eliminado con éxito.")
        
        return redirect('/presupuestos/')  # Ajusta esto según tu vista de lista

    return redirect('/presupuestos/')  # Redirige en caso de solicitud no POST

@login_required
@permission_required('inicio.view_cliente', login_url='', raise_exception=True)
def editarPresupuesto(request):
    if request.method == 'POST':
        id_presupuesto = request.POST.get('id_presupuesto')
        monto_total_presupuesto = request.POST.get('totalCostEditar')
        id_edificio = request.POST.get('edificio_asignado_editar')
        id_empleado = request.POST.get('vendedor_asignado_editar')

        lista_cantidad_detalle_presupuesto = request.POST.getlist('cantidades_editar[]')
        costos_extra = request.POST.getlist('costos_extra_editar[]')
        lista_precio_total_detalle_presupuesto = request.POST.getlist('subtotales_editar[]')
        lista_id_servicio = request.POST.getlist('servicios_editar[]')
        lista_id_detalles = request.POST.getlist('id_detalles_editar[]')

        # Lógica para crear la lista de detalles del presupuesto
        lista_detalles = [
            {
                'id_detalle_presupuesto': id_detalle,
                'id_servicio': id_servicio,
                'cantidad': cantidad,
                'costos_extra': costo_extra,
                'precio_total': precio_total
            }
            for id_detalle, id_servicio, cantidad, costo_extra, precio_total in zip(
                lista_id_detalles,
                lista_id_servicio,
                lista_cantidad_detalle_presupuesto,
                costos_extra,
                lista_precio_total_detalle_presupuesto
            )
        ]

        # Obtener el tipo de acción: editar o enviar a ventas
        action_type = request.POST.get('action_type')

        if action_type == 'editar':
            # Si el botón presionado es "Editar Presupuesto"
            resultado = Presupuesto.actualizarPresupuesto(id_presupuesto, monto_total_presupuesto, id_edificio, id_empleado, lista_detalles)
            if resultado:
                messages.success(request, 'El presupuesto se actualizó correctamente.')
            else:
                messages.error(request, 'Hubo un error al actualizar el presupuesto.')
            return redirect('/presupuestos/')

        elif action_type == 'enviarVentas':
            # Redirigir a la vista de enviar a ventas
            return redirect('presupuestos:enviarVentas', id_presupuesto=id_presupuesto)

    return redirect('/presupuestos/')


@login_required
@permission_required('inicio.view_cliente', login_url='', raise_exception=True)
def obtenerPresupuesto(request, id_presupuesto):
    if request.method == 'GET':
        # Obtener el presupuesto y los detalles asociados usando el ORM
        presupuesto = get_object_or_404(Presupuesto, id_presupuesto=id_presupuesto)
        detalles_presupuesto = DetallePresupuesto.objects.filter(id_presupuesto=id_presupuesto)

        # Obtener el edificio y el cliente relacionado
        edificio = get_object_or_404(Edificio, id_edificio=presupuesto.id_edificio)
        id_cliente = edificio.id_cliente_id  # Suponiendo que id_cliente está en el modelo Edificio
        
        # Preparar los datos del presupuesto
        presupuesto_data = {
            'id_presupuesto': presupuesto.id_presupuesto,
            'fecha_hora': presupuesto.fecha_hora_presupuesto,
            'monto_total': presupuesto.monto_total_presupuesto,
            'id_edificio': presupuesto.id_edificio,
            'id_vendedor': presupuesto.id_empleado,
            'id_cliente': id_cliente  # Asegúrate de que esto sea un valor simple
        }

        # Preparar los detalles del presupuesto
        detalles = [
            {   
                'id_detalle_presupuesto': detalle.id_detalle_presupuesto,
                'cantidad': detalle.cantidad_detalle_presupuesto,
                'costo_extra': detalle.costo_extra_presupuesto,
                'precio_total': detalle.precio_total_detalle_presupuesto,
                'id_servicio': detalle.id_servicio
            }
            for detalle in detalles_presupuesto
        ]
        
        # Preparar el contexto para la respuesta JSON
        context = {
            'presupuesto': presupuesto_data,
            'detalles': detalles
        }

        # Devolver la respuesta JSON
        return JsonResponse(context, safe=False)

    # Manejar casos donde el método de solicitud no sea GET
    return JsonResponse({'error': 'Método de solicitud no válido'}, status=405)

@login_required
@permission_required('inicio.view_cliente', login_url='', raise_exception=True)
def enviarVentas(request, id_presupuesto):
    print(f"ID Presupuesto recibido en enviarVentas: {id_presupuesto}")  # Imprimir el id_presupuesto
    id_venta = Presupuesto.enviarVentas(id_presupuesto)
    if id_venta:
        print(f"Venta creada con ID: {id_venta}")  # Imprimir el id de la venta creada
        messages.success(request, 'El presupuesto se ha transferido a ventas exitosamente.')
        return redirect('/ventas/')
    else:
        print("Error al crear la venta.")  # Imprimir mensaje de error
        return redirect('/presupuestos/')

@login_required
@permission_required('inicio.view_cliente', login_url='', raise_exception=True)
def eliminarDetallePresupuesto(request, id_detalle):
    if request.method == 'DELETE':
        # Obtener el detalle correspondiente
        detalle = get_object_or_404(DetallePresupuesto, id_detalle_presupuesto=id_detalle)
        

        # Intentar eliminar el detalle
        try:
            detalle.delete()
            return JsonResponse({'message': 'El detalle de presupuesto se eliminó correctamente.'}, status=200)
        except Exception as e:
            print("Error al eliminar detalle:", e)
            return JsonResponse({'message': f'Error al eliminar el detalle de presupuesto: {str(e)}'}, status=500)


    return JsonResponse({'message': 'Método no permitido.'}, status=405)

def agregarObservacionPresupuesto(request, id_detalle_presupuesto):
    if request.method == 'POST':
        descripcion_observacion = request.POST.get('descripcion_observacion')
        DetallePresupuesto.agregarObservacionPresupuesto(id_detalle_presupuesto, descripcion_observacion)
    return redirect('/presupuestos/')