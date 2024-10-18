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
      print(ventas)
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

    # Accede al primer detalle de la venta
    detalle_venta = venta['detalles'][0]

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
            "condicion_pago": venta['cod_metodo_pago'],
            "condicion_iva": "CF"
        },
        "comprobante": {
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "vencimiento": "26/03/2028",
            "tipo": "FACTURA C",
            "operacion": "V",
            "punto_venta": "00679",  
            "numero": "00000019",
            "moneda": "PES",
            "cotizacion": 1,
            "periodo_facturado_desde": venta['fecha_hora_venta'].strftime("%d/%m/%Y"),
            "periodo_facturado_hasta": venta['fecha_hora_venta'].strftime("%d/%m/%Y"),
            "rubro": "Servicios",
            "rubro_grupo_contable": "Servicios",
            "detalle": [
                {
                    "cantidad": str(detalle_venta['cantidad_detalle_venta']),
                    "producto": {
                        "descripcion": detalle_venta['nombre_servicio'],
                        "unidad_bulto": "1",
                        "lista_precios": "Lista de precios API 3",
                        "codigo": "1",  # Código del servicio, si está disponible
                        "precio_unitario_sin_iva": str(detalle_venta['precio_detalle_venta']),
                        "alicuota": "0"
                    },
                    "leyenda": ""
                },
                {
                    "cantidad": "1",
                    "producto": {
                        "descripcion": "Costo extra por servicio",
                        "unidad_bulto": "1",
                        "lista_precios": "Lista de precios API 3",
                        "codigo": "99999",  # Usar un código genérico o uno especial
                        "precio_unitario_sin_iva": str(detalle_venta['costo_extra_detalle_venta']),
                        "alicuota": "0"
                    },
                    "leyenda": ""
                }
            ],
            "bonificacion": "0.00",
            "leyenda_gral": " ",
            "total": str(venta['monto_total_venta'])
        }
    }

    # Realiza la petición HTTP
    conn = http.client.HTTPSConnection("www.tusfacturas.app")
    headers = {'Content-Type': "application/json"}
    
    conn.request("POST", "/app/api/v2/facturacion/nuevo", json.dumps(payload), headers)
    res = conn.getresponse()
    data = res.read()

    return JsonResponse(data.decode("utf-8"), safe=False)


def editarVenta(request, id_venta):
    if request.method == 'POST':
        metodo_pago = request.POST.get('metodo_pago')
        estado_venta = request.POST.get('estado_venta')
        # ... (obten el resto de los datos necesarios y actualiza la venta)
        
        # Lógica para actualizar la venta
        # Asegúrate de usar el id_venta para encontrar la venta correspondiente y hacer la actualización
        try:
            venta = Venta.objects.get(id_venta=id_venta)
            venta.metodo_pago = metodo_pago
            venta.estado_venta = estado_venta
            venta.save()
            messages.success(request, 'La venta se actualizó correctamente.')
        except Venta.DoesNotExist:
            messages.error(request, 'No se encontró la venta.')
        
        return redirect('/ventas/')

    return redirect('/ventas/')  # Redirige si no es una petición POST
