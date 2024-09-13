from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Presupuesto, DetallePresupuesto
from django.contrib import messages
from ..clientes.models import Cliente, Edificio
from ..empleados.models import Empleado
from ..servicios.models import Servicio, CategoriaServicio
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
    #fecha_hora_presupuesto, monto_total_presupuesto, id_edificio, id_empleado, lista_detalles
    if request.method == 'POST':
        fecha_hora_presupuesto = request.POST.get('fecha_hora_presupuesto')
        monto_total_presupuesto = request.POST.get('monto_total_presupuesto')
        id_edificio = request.POST.get('id_edificio')
        id_empleado = request.POST.get('id_empleado')

        #cantidad_detalle_presupuesto, precio_unitario_detalle_presupuesto, precio_total_detalle_presupuesto, , id_servicio
        lista_cantidad_detalle_presupuesto = request.POST.getlist('lista_cantidad_detalle_presupuesto[]')
        lista_precio_unitario_detalle_presupuesto = request.POST.getlist('lista_precio_unitario_detalle_presupuesto[]')
        lista_precio_total_detalle_presupuesto = request.POST.getlist('lista_precio_unitario_detalle_presupuesto[]')
        lista_id_servicio = request.POST.getlist('lista_id_servicio[]')
        
        # Crear una lista de detalles
        lista_detalles = list(zip(lista_cantidad_detalle_presupuesto, lista_precio_unitario_detalle_presupuesto, lista_precio_total_detalle_presupuesto, lista_id_servicio))
        id_presupuesto = Presupuesto.insertarPresupuesto(fecha_hora_presupuesto, monto_total_presupuesto, id_edificio, id_empleado, lista_detalles)
        if id_presupuesto:
            messages.success(request, 'El presupuesto se agregó correctamente.')
            return redirect('/presupuestos/')
        else:
            messages.error(request, 'Hubo un error al agregar el presupuesto.')
            return redirect('/presupuestos/')
    else:
        presupuestos = Presupuesto.listarPresupuestos()
        return render(request, 'agregarPresupuesto.html', {'presupuestos': presupuestos})

def mostrar_vendedores(request, method='GET'):
    vendedores = list(
        Empleado.objects.select_related('id_persona').filter(id_tipo_empleado=1).values(
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
             messages.error(request, "No se puede eliminar el presupuesto porque está referenciado en uno o más servicios.")
            
        else:
            presupuesto.delete()
            messages.success(request, "Presupuesto eliminado con éxito.")
        
        return redirect('/presupuestos/')  # Ajusta esto según tu vista de lista

    return redirect('/presupuestos/')  # Redirige en caso de solicitud no POST
