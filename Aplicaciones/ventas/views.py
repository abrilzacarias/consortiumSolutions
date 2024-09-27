from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from Aplicaciones.presupuestos.models import Presupuesto, DetallePresupuesto
from .models import Venta  # Asegúrate de importar Venta
from django.contrib import messages
from ..clientes.models import Cliente, Edificio
from ..empleados.models import Empleado
from ..servicios.models import CategoriaServicio

# Create your views here.
def home(request):
    # Llamamos al método listarVentas para obtener las ventas
    ventas = Venta.listarVentas()
    
    # Retornamos la plantilla con las ventas en el contexto
    return render(request, 'ventasViews.html', {'ventas': ventas})
