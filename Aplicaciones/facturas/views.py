from django.shortcuts import render
from .models import Facturas
# Create your views here.

def listarFacturas(request):
    resultados = Facturas.listarFacturas()
    
    facturas = {
    str(entry[0]): {  # Usar el numero_comprobante como clave
        'numero_comprobante': entry[1],
        'fecha_emision': entry[2],
        'nombre_cliente': entry[3],
        'apellido_cliente': entry[4],
        'nombre_edificio': entry[5],
        'descarga_ticket': entry[6]
    }
    for entry in resultados
    }
    print(facturas)

    return render(request, 'vistaFacturas.html', {'facturas': facturas}) 