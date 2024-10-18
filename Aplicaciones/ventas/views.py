from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from Aplicaciones.presupuestos.models import Presupuesto, DetallePresupuesto
from .models import Venta  # Asegúrate de importar Venta
from django.contrib import messages
from ..clientes.models import Cliente, Edificio
from ..empleados.models import Empleado
from ..servicios.models import CategoriaServicio
from ..inicio.views import paginacionTablas
import http.client, json
from datetime import datetime

def home(request):
      ventas = Venta.listarVentas()
     # print(ventas)
      context = paginacionTablas(request, ventas, 'ventas')
      return render(request, 'ventasViews.html', context)

def enviar_factura_prueba(request): 
    # Datos ficticios para la prueba
    ventas = Venta.listarVentas()  # Obtiene todas las ventas
    
    # Asegúrate de que haya al menos una venta para evitar errores
    if not ventas:
        return JsonResponse({'error': 'No hay ventas disponibles'}, status=404)

    # Selecciona la primera venta para esta prueba
    venta = ventas[0]

    payload = {
        "usertoken": "b436f25f0f4b57cd11e428d84dc1e88b653c4129e6b08addff425399829b4c7f",
        "apikey": "64949",
        "apitoken": "b6f0ac307a7b6da895b6e329bc5d3f83",
        "cliente": {
            "documento_tipo": "CUIT",
            "documento_nro": venta['cuit_edificio'],
            "razon_social": venta['nombre_edificio'],
            "email": "cliente@prueba.com",
            "domicilio": venta['direccion_edificio'],
            "provincia": "2",
            "envia_por_mail": "N",
            "condicion_pago": "202",  
            "condicion_iva": "CF"     
        },
        "comprobante": {
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "vencimiento": "26/03/2028",
            "tipo": "FACTURA C",
            "operacion": "V",
            "punto_venta": "00679",  
            "numero": "00000015",
            "moneda": "PES",
            "cotizacion": 1,
            "periodo_facturado_desde": venta['fecha_hora_venta'].strftime("%d/%m/%Y"),
            "periodo_facturado_hasta": venta['fecha_hora_venta'].strftime("%d/%m/%Y"),
            "rubro": "Servicios",
            "rubro_grupo_contable": "Servicios",
            "detalle": [],  # Inicializa la lista de detalles
            "bonificacion": "0.00",
            "leyenda_gral": " ",
            "total": str(venta['monto_total_venta'])
        }
    }

    # Agrega los detalles de la venta al payload
    for detalle in venta['detalles']:
        detalle_item = {
            "cantidad": str(detalle['cantidad_detalle_venta']),
            "producto": {
                "descripcion": venta['nombre_servicio'],
                "unidad_bulto": "1",
                "lista_precios": "Lista de precios API 3",
                "codigo": str(venta['cod_servicio']),
                "precio_unitario_sin_iva": str(detalle['precio_detalle_venta']),
                "alicuota": "0"
            },
            "leyenda": ""
        }
        payload["comprobante"]["detalle"].append(detalle_item)

    # Realiza la petición HTTP
    conn = http.client.HTTPSConnection("www.tusfacturas.app")
    headers = {'Content-Type': "application/json"}
    
    conn.request("POST", "/app/api/v2/facturacion/nuevo", json.dumps(payload), headers)
    res = conn.getresponse()
    data = res.read()

    return JsonResponse(data.decode("utf-8"), safe=False)
