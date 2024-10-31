from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import MetodoPago, Venta, EstadoVenta, RegistroEstadoVenta, DetalleVenta  # Asegúrate de importar la clase MetodoPago
from django.contrib import messages
from ..facturas.models import Factura
from ..inicio.views import paginacionTablas
import http.client, json
from datetime import datetime


def home(request):
    ventas = Venta.listarVentas()
    metodos_pago = MetodoPago.obtenerMetodosPago() # Asegúrate de incluir esto
    estados_venta = EstadoVenta.obtenerEstadosVenta()
    context = paginacionTablas(request, ventas, 'ventas')
    context['metodos_pago'] = metodos_pago  # Agrega métodos de pago al contexto
    context['estados_venta'] = estados_venta
    # Asegúrate de que en tu vista 'home' o en la vista correspondiente
    #context['detalles'] = detalle_venta_queryset  # Asegúrate de que incluye el id_estado_venta
    return render(request, 'ventasViews.html', context)


def enviar_factura_prueba(request, id_venta):
    ultimo = Factura.obtenerUltimoComprobanteFactura()
    ultimo_comprobante = int(ultimo[0][0]) + 1  # Sumar 1 al último comprobante
    siguiente_comprobante = str(ultimo_comprobante).zfill(8)  # Formatear con ceros a la izquierda

    ventas = Venta.listarVentas()
    venta = next((v for v in ventas if v['id_venta'] == id_venta), None)
    print(venta)
    if not venta:
        messages.error(request, 'Venta no encontrada.')
        return redirect('ruta_a_ventasViews')  # Reemplaza con la URL a ventasViews.html
    if not venta.get('detalles'):
        messages.error(request, 'No hay detalles disponibles para esta venta.')
        return redirect('ruta_a_ventasViews')

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

        if 'costo_extra_detalle_venta' in detalle_venta:
            detalles_payload.append({
                "cantidad": "1",
                "producto": {
                    "descripcion": "Costo extra por servicio",
                    "unidad_bulto": "1",
                    "lista_precios": "Lista de precios API 3",
                    "codigo": "0",
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
            "numero": siguiente_comprobante,
            "moneda": "PES",
            "cotizacion": 1,
            "periodo_facturado_desde": venta['fecha_hora_venta'].strftime("%d/%m/%Y"),
            "periodo_facturado_hasta": venta['fecha_hora_venta'].strftime("%d/%m/%Y"),
            "rubro": "Servicios",
            "rubro_grupo_contable": "Servicios",
            "detalle": detalles_payload,
            "bonificacion": "0.00",
            "leyenda_gral": " ",
            "total": str(venta['monto_total_venta'])
        }
    }

    conn = http.client.HTTPSConnection("www.tusfacturas.app")
    headers = {'Content-Type': "application/json"}
    conn.request("POST", "/app/api/v2/facturacion/nuevo", json.dumps(payload), headers)
    res = conn.getresponse()
    data = res.read()
    response_data = json.loads(data.decode("utf-8"))
    print(response_data)
    if response_data.get("error") == "N":
        link_descarga_ticket = response_data.get('comprobante_ticket_url', '')
        numero_comprobante = response_data.get('comprobante_nro', '')
        link_descarga_factura = response_data.get('comprobante_pdf_url', '')
        numero_comprobante_final = numero_comprobante.split("-")[1]

        estado_pago = 1
        Factura.agregarFactura(numero_comprobante_final, id_venta, venta['monto_total_venta'], venta['monto_total_venta'], link_descarga_ticket, estado_pago)

        messages.success(request, f'La factura {numero_comprobante} se generó y guardó correctamente.')
    else:
        messages.error(request, 'Hubo un problema al generar la factura.')

    return redirect('ventas:home')  


def editarMetodoPago(request, id_venta):
    if request.method == 'POST':
        # Imprimir todos los datos que llegan en el POST
        print(request.POST)  # Esto te mostrará todos los datos enviados por el formulario

        # Obtener el nuevo método de pago del formulario
        id_nuevo_metodo_pago = request.POST.get('metodo_pago')  # Cambia 'id_metodo_pago' por 'metodo_pago'
        
        # Llama al método de clase para actualizar el método de pago
        Venta.actualizarMetodoPago(id_nuevo_metodo_pago, id_venta)
        
        # Redirige a la vista principal de ventas
        return redirect('ventas:home')  # Asegúrate de que 'ventas:home' esté definido en tus URLs

    else:
        # En caso de que sea un GET, obtén los métodos de pago y la venta
        metodos_pago = MetodoPago.obtenerMetodosPago()
        venta = get_object_or_404(Venta, id_venta=id_venta)

        # Prepara el contexto para la plantilla
        context = {
            'metodos_pago': metodos_pago,
            'venta': venta,
        }
        return render(request, 'ventas/ventasViews.html', context)



def cambiarEstadoRegistroVenta(request, id_detalle_venta):
    if request.method == 'POST':
        # Obtener los datos enviados desde el formulario
        id_nuevo_estado_venta = request.POST.get('estado_venta')
        id_empleado = request.user.id_empleado if hasattr(request.user, 'id_empleado') else None  # Asume que el empleado está relacionado con el usuario actual

        # Llama al método para registrar el cambio de estado
        RegistroEstadoVenta.registrarCambioEstado(id_detalle_venta, id_nuevo_estado_venta, id_empleado)

        # Redirige a la vista de la venta o cualquier otra página
        return redirect('ventas:home')

    # Si no es un POST, redirige o maneja de otra manera
    return redirect('ventas:home')

def agregarObservacionDetalleVenta(request, id_detalle_venta):
    if request.method == 'POST':
        descripcion_observacion = request.POST.get('descripcion_observacion')
        DetalleVenta.agregarObservacionDetalleVenta(id_detalle_venta, descripcion_observacion)
    return redirect('/ventas/')