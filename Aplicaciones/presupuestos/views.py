from django.shortcuts import render, redirect
from .models import Presupuesto, DetallePresupuesto
from django.contrib import messages

# Create your views here.
def home(request):
    
    presupuestos = Presupuesto.listarPresupuestos()
    detalle_presupuesto = DetallePresupuesto.listarDetallePresupuesto()
    print(detalle_presupuesto)
    return render(request, 'listarPresupuestos.html', {'presupuestos': presupuestos})


def detalle_presupuesto(request, id_presupuesto): 
    
    detalle_presupuesto = [detalle for detalle in DetallePresupuesto.listarDetallePresupuesto() if detalle['id_presupuesto'] == id_presupuesto]
    total_presupuesto = sum(detalle['cantidad_detalle_presupuesto'] * detalle['precio_unitario_detalle_presupuesto'] for detalle in detalle_presupuesto)
    return render(request, 'detallePresupuesto.html', {'detalle_presupuesto': detalle_presupuesto, 'total_presupuesto': total_presupuesto})

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