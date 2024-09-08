from django.shortcuts import render
from .models import Presupuesto, DetallePresupuesto

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