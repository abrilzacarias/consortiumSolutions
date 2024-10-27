from django.shortcuts import render, get_object_or_404, redirect
from .models import EstadoFactura, Factura
import mercadopago
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse, Http404





def listarFacturas(request):
    resultados = Factura.listarFacturas()
    estados_factura = EstadoFactura.objects.all()
    facturas = {
        str(entry[0]): {  # Usar id como clave
            'numero_comprobante': entry[1],
            'fecha_emision_factura': entry[2],
            'nombre_cliente': entry[3],
            'apellido_cliente': entry[4],
            'nombre_edificio': entry[5],
            'descarga_ticket': entry[6],
            'id_estado_factura' : entry[7],
            'descripcion_estado_factura' : entry[8], 
            'nombres_servicios' : entry[9], 
            'cantidades_servicios' : entry[10], 
            'precios_totales_servicios' : entry[11]
        }
        for entry in resultados
    }
    
    # Llama a la función para generar el link de pago
    #payment_link = generar_link_pago()
  
    #print(payment_link)
    return render(request, 'vistaFacturas.html', {'facturas': facturas, 'estados_factura': estados_factura}) 

def generar_link_pago(request, id_factura):
    try:
        # Obtener todas las facturas
        facturas = Factura.listarFacturas()
        
        # Buscar la factura específica
        vista_factura = None
        for factura in facturas:
            if factura[0] == id_factura:  # Asumiendo que el ID es el primer elemento
                vista_factura = factura
                break
        
        if not vista_factura:
            raise Http404("Factura no encontrada")

        # Extraer los datos de la tupla
        nombres_servicios = vista_factura[9].split(", ")  # 'Reparación de pisos, Limpieza de Vidrios'
        cantidades_servicios = vista_factura[10].split(", ")  # '1, 1'
        precios_totales_servicios = vista_factura[11].split(", ")  # '105, 85'

        sdk = mercadopago.SDK("TEST-1083456035276298-101922-810a2e0aeb770bbf8ed3191b3cd59702-566328219")

        items = []
        for nombre, cantidad, precio in zip(nombres_servicios, cantidades_servicios, precios_totales_servicios):
            items.append({
                "title": nombre,
                "quantity": 1,
                "unit_price": float(precio),
                "currency_id": "ARS"
            })

        preference_data = {
            "items": items,
            "payer": {
                "email": "test_user_123456@testuser.com"
            }
        }

        # Debug prints
        print("Items:", items)
        print("Preference data:", preference_data)

        preference = sdk.preference().create(preference_data)
        print("Full Mercado Pago response:", preference)
        payment_link = preference["response"].get("init_point")
        print(payment_link)
        
        return JsonResponse({"payment_link": payment_link})
        
    except Exception as e:
        print(f"Error detallado: {str(e)}")
        return JsonResponse({"error": str(e)}, status=400)


def actualizar_estado_factura(request, id_factura):
    if request.method == 'POST':
        # Obtener el nuevo ID del estado desde el formulario
        nuevo_estado_id = request.POST.get('id_estado_factura')

        if nuevo_estado_id:
            # Obtener la factura correspondiente usando su ID
            factura = get_object_or_404(Factura, id_factura=id_factura)
            
            # Obtener la instancia del estado correspondiente
            estado_factura = get_object_or_404(EstadoFactura, id_estado_factura=nuevo_estado_id)
            
            # Actualizar el estado de la factura
            factura.id_estado_factura = estado_factura  # Asignar la instancia
            factura.save()

            # Mensaje de éxito
            messages.success(request, 'Estado de la factura actualizado correctamente.')
        else:
            messages.error(request, 'Debe seleccionar un estado válido.')

        return redirect(reverse('facturas:listarFacturas'))

    return redirect(reverse('facturas:listarFacturas'))