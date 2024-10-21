from django.shortcuts import render
from .models import Facturas, EstadoFactura
import mercadopago

def listarFacturas(request):
    resultados = Facturas.listarFacturas()
    estados_factura = EstadoFactura.objects.all()
    print(estados_factura)
    facturas = {
        str(entry[0]): {  # Usar id como clave
            'numero_comprobante': entry[1],
            'fecha_emision': entry[2],
            'nombre_cliente': entry[3],
            'apellido_cliente': entry[4],
            'nombre_edificio': entry[5],
            'descarga_ticket': entry[6],
            'id_estado_factura' : entry[7],
            'descripcion_estado_factura' : entry[8]
        }
        for entry in resultados
    }
    
    # Llama a la función para generar el link de pago
    payment_link = generar_link_pago()

    return render(request, 'vistaFacturas.html', {'facturas': facturas, 'estados_factura': estados_factura, 'payment_link': payment_link}) 

def generar_link_pago():
    sdk = mercadopago.SDK("TEST-1083456035276298-101922-810a2e0aeb770bbf8ed3191b3cd59702-566328219")
    
    # Crea un objeto de preferencia de pago
    preference_data = {
        "items": [
            {
                "title": "Producto de ejemplo",
                "quantity": 1,
                "unit_price": 100,
                "currency_id": "ARS"
            }
        ],
        "payer": {
            "email": "test_user_123456@testuser.com"
        }
    }

    # Realiza la solicitud para crear la preferencia de pago
    preference = sdk.preference().create(preference_data)

    # Imprime la respuesta completa para depuración
    '''print("Respuesta de Mercado Pago:", preference)'''

    # Obtén el link de pago si existe
    payment_link = preference["response"].get("init_point")

    '''if payment_link:
        print("Link de Pago:", payment_link)
    else:
        print("No se pudo obtener el link de pago.")'''
    
    return payment_link