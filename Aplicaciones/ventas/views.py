from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Venta  # Asegúrate de importar Venta
from django.contrib import messages
from ..facturas.models import Facturas
from ..inicio.views import paginacionTablas
import http.client, json
from datetime import datetime

def home(request):
      ventas = Venta.listarVentas()
      print(ventas)
      context = paginacionTablas(request, ventas, 'ventas')
      return render(request, 'ventasViews.html', context)

def enviar_factura_prueba(request, id_venta): 
    # Obtiene todas las ventas
    ventas = Venta.listarVentas()  
    
    # Busca la venta específica por id_venta
    venta = next((v for v in ventas if v['id_venta'] == id_venta), None)

    # Asegúrate de que se encontró la venta
    if not venta:
        return JsonResponse({'error': 'Venta no encontrada'}, status=404)

    # Asegúrate de que haya al menos un detalle en la venta
    if not venta.get('detalles'):
        return JsonResponse({'error': 'No hay detalles disponibles para esta venta'}, status=404)

    # Preparar el detalle en el formato necesario
    detalles_payload = []
    for detalle_venta in venta['detalles']:
        detalles_payload.append({
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
        })
        
        # Añadir costo extra si está presente
        if 'costo_extra_detalle_venta' in detalle_venta:
            detalles_payload.append({
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
            })

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
            "numero": "00000029",
            "moneda": "PES",
            "cotizacion": 1,
            "periodo_facturado_desde": venta['fecha_hora_venta'].strftime("%d/%m/%Y"),
            "periodo_facturado_hasta": venta['fecha_hora_venta'].strftime("%d/%m/%Y"),
            "rubro": "Servicios",
            "rubro_grupo_contable": "Servicios",
            "detalle": detalles_payload,  # Usamos todos los detalles aquí
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
    response_data = json.loads(data.decode("utf-8"))
    link_descarga_factura = response_data.get('comprobante_ticket_url', '')
    numero_comprobante = response_data.get('comprobante_nro', '')
    numero_comprobante_final = numero_comprobante.split("-")[1] 
    print(f'AAAAAAAAAAA{link_descarga_factura}')

    print(response_data)
    Facturas.agregarFactura(numero_comprobante_final, id_venta, venta['monto_total_venta'], venta['monto_total_venta'], link_descarga_factura)
    

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
