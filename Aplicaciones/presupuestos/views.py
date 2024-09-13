from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Presupuesto, DetallePresupuesto
from django.contrib import messages
from ..clientes.models import Clientes
from ..empleados.models import Empleado
from ..servicios.models import Servicio
# Create your views here.
def home(request):
    presupuestos = Presupuesto.listarPresupuestos()
    #print(detalle_presupuesto)
    return render(request, 'listarPresupuestos.html', {'presupuestos': presupuestos})

def detalle_presupuesto(id_presupuesto): 
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
    vendedores = list(Empleado.objects.values('id_empleado', 'nombre_persona', 'apellido_persona'))
    for vendedor in vendedores:
        print(vendedor)
    return JsonResponse(vendedores, safe=False)

def mostrar_servicios(request, method='GET'):
    servicios = list(Servicio.objects.values('id_servicio', 'nombre_servicio'))
    for servicio in servicios:
        print(servicio)
    return JsonResponse(servicios, safe=False)

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