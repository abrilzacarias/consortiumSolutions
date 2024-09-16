from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Presupuesto, DetallePresupuesto
from django.contrib import messages
from ..clientes.models import Cliente, Edificio
from ..empleados.models import Empleado
from ..servicios.models import CategoriaServicio
# Create your views here.
def home(request):
    presupuestos = Presupuesto.listarPresupuestos()
    #print(detalle_presupuesto)
    return render(request, 'listarPresupuestos.html', {'presupuestos': presupuestos})

def detalle_presupuesto(request, id_presupuesto): 
    detalle_presupuesto = [detalle for detalle in DetallePresupuesto.listarDetallePresupuesto() if detalle['id_presupuesto'] == id_presupuesto]
    print(detalle_presupuesto)
    return JsonResponse(detalle_presupuesto, safe=False)

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
                'precio_unitario': costos_extra,
                'precio_total': precio_total
            }
            for id_servicio, cantidad, costos_extra, precio_total in zip(
                lista_id_servicio,
                lista_cantidad_detalle_presupuesto,
                costos_extra,
                lista_precio_total_detalle_presupuesto
            )
        ]
        print(lista_detalles)
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

def mostrar_vendedores(request, method='GET'):
    vendedores = list(
        Empleado.objects.select_related('id_persona').filter(tipo_empleado_id=1).values(
            'id_empleado',
            'id_persona__nombre_persona',  # Accediendo al nombre de la tabla Persona
            'id_persona__apellido_persona'  # Accediendo al apellido de la tabla Persona
        )
    )
    for vendedor in vendedores:
        print(vendedor)

    return JsonResponse(vendedores, safe=False)


def mostrar_clientes(request, method='GET'):
    servicios = list(Cliente.objects.select_related('id_persona').values('id_cliente', 'id_persona__nombre_persona', 'id_persona__apellido_persona'))
    for servicio in servicios:
        print(servicio)
    return JsonResponse(servicios, safe=False)

def mostrar_edificios(request, id_cliente):
    edificios = list(Edificio.objects.filter(id_cliente=id_cliente).values('id_edificio', 'nombre_edificio'))
    print(edificios)
    return JsonResponse(edificios, safe=False)

def obtener_servicios(request):
    categorias = CategoriaServicio.objects.prefetch_related('servicio').all()
    
    response_data = []
    
    for categoria in categorias:
        servicios = categoria.servicio.all()
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

def eliminarPresupuesto(request, id_presupuesto):
    if request.method == 'POST':
        presupuesto = get_object_or_404(Presupuesto, id_presupuesto=id_presupuesto)
        
        # Verifica si el presupuesto está referenciado en MensajePresupuesto
        detalles = DetallePresupuesto.objects.filter(id_presupuesto=presupuesto.id_presupuesto)
        print(detalles)
        if detalles.exists():
             detalles.delete()
             presupuesto.delete()
             messages.success(request, "Presupuesto y detalles eliminados con éxito.")
        else:
            presupuesto.delete()
            messages.success(request, "Presupuesto eliminado con éxito.")
        
        return redirect('/presupuestos/')  # Ajusta esto según tu vista de lista

    return redirect('/presupuestos/')  # Redirige en caso de solicitud no POST

def editarPresupuesto(request):
    if request.method == 'POST':
        id_presupuesto = request.POST.get('id_presupuesto')
        print(id_presupuesto)
        monto_total_presupuesto = request.POST.get('totalCostEditar')
        id_edificio = request.POST.get('edificio_asignado_editar')
        id_empleado = request.POST.get('vendedor_asignado_editar')
        
        lista_cantidad_detalle_presupuesto = request.POST.getlist('cantidades_editar[]')
        costos_extra = request.POST.getlist('costos_extra_editar[]')
        lista_precio_total_detalle_presupuesto = request.POST.getlist('subtotales_editar[]')
        lista_id_servicio = request.POST.getlist('servicios_editar[]')
        lista_id_detalles = request.POST.getlist('id_detalles_editar[]')
        print(monto_total_presupuesto)
        print(id_edificio)
        print(id_empleado)
        print(lista_cantidad_detalle_presupuesto)
        print(f"costos_extra: {costos_extra}")
        print(f"lista_precio_total_detalle_presupuesto: {lista_precio_total_detalle_presupuesto}")
        print(f'lista_id_servicio: {lista_id_servicio}')
        print(f'lista_id_detalles: {lista_id_detalles}')
        
        lista_detalles = [
            {   
                'id_detalle_presupuesto': lista_id_detalles,
                'id_servicio': id_servicio,
                'cantidad': cantidad,
                'precio_unitario': precio_unitario,
                'precio_total': precio_total
            }
            for lista_id_detalles, id_servicio, cantidad, precio_unitario, precio_total in zip(
                lista_id_detalles,
                lista_id_servicio,
                lista_cantidad_detalle_presupuesto,
                costos_extra,
                lista_precio_total_detalle_presupuesto
            )
        ]

        print(f'lista_detalles: {lista_detalles}')

        resultado = Presupuesto.actualizarPresupuesto(id_presupuesto, monto_total_presupuesto, id_edificio, id_empleado, lista_detalles)
        if resultado:
            messages.success(request, 'El presupuesto se actualizó correctamente.')
            return redirect('/presupuestos/')
        else:
            messages.error(request, 'Hubo un error al actualizar el presupuesto.')
        return redirect('/presupuestos/')

def obtenerPresupuesto(request, id_presupuesto):
    if request.method == 'GET':
        # Obtener el presupuesto y los detalles asociados usando el ORM
        presupuesto = get_object_or_404(Presupuesto, id_presupuesto=id_presupuesto)
        detalles_presupuesto = DetallePresupuesto.objects.filter(id_presupuesto=id_presupuesto)

        # Obtener el edificio y el cliente relacionado
        edificio = get_object_or_404(Edificio, id_edificio=presupuesto.id_edificio)
        id_cliente = edificio.id_cliente_id  # Suponiendo que `id_cliente` está en el modelo Edificio
        
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
                'costo_extra': detalle.precio_unitario_detalle_presupuesto,
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