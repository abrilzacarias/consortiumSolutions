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
    
    context = paginacionTablas(request, ventas, 'ventas')
    return render(request, 'ventasViews.html', context)

def enviar_factura_prueba(request): 
    # Datos ficticios para la prueba
    ventas = Venta.listarVentas()[0]  # Selecciona la primera venta para esta prueba
    
    payload = {
   "usertoken":"b436f25f0f4b57cd11e428d84dc1e88b653c4129e6b08addff425399829b4c7f",
   "apikey":"64949",
   "apitoken":"b6f0ac307a7b6da895b6e329bc5d3f83",
   "cliente": {
      "documento_tipo":"CUIT",
      "documento_nro":ventas['cuit_edificio'],
      "razon_social":ventas['nombre_edificio'],
      "email":"cliente@prueba.com",
      "domicilio": ventas['direccion_edificio'],
      "provincia":"2",
      "envia_por_mail":"N",
      "condicion_pago":"202",  
      "condicion_iva":"CF"     
   },
   "comprobante": {
      "fecha":datetime.now().strftime("%d/%m/%Y"),
      "vencimiento":"26/03/2028",
      "tipo":"FACTURA C",
      "operacion":"V",
      "punto_venta":"00679",  
      "numero":"00000015",
      "moneda":"PES",
      "cotizacion": 1,
      "periodo_facturado_desde":ventas['fecha_hora_venta'].strftime("%d/%m/%Y"),
      "periodo_facturado_hasta":ventas['fecha_hora_venta'].strftime("%d/%m/%Y"),
      "rubro":"Servicios",
      "rubro_grupo_contable":"Servicios",
      "detalle":[
         {
            "cantidad":str(ventas['cantidad_detalle_venta']),
            "producto":{
               "descripcion":ventas['nombre_servicio'],
               "unidad_bulto":"1",
               "lista_precios":"Lista de precios API 3",
               "codigo":str(ventas['cod_servicio']),
               "precio_unitario_sin_iva":str(ventas['precio']),
               "alicuota":"0"
            },
            "leyenda":""
         },
      ],
      "bonificacion":"0.00",
      "leyenda_gral":" ",
      "total":str(ventas['monto_total_venta'])
   }
}


    # Realiza la petición HTTP
    conn = http.client.HTTPSConnection("www.tusfacturas.app")
    headers = {'Content-Type': "application/json"}
    
    conn.request("POST", "/app/api/v2/facturacion/nuevo", json.dumps(payload), headers)
    res = conn.getresponse()
    data = res.read()

    return JsonResponse(data.decode("utf-8"), safe=False)

