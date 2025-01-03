from django.shortcuts import render, get_object_or_404, redirect
from .models import EstadoFactura, Factura
import mercadopago
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse, Http404
from ..inicio.views import paginacionTablas
from django.contrib.auth.decorators import login_required, permission_required

#TODO @permission_required('inicio.view_detalleventa', login_url='', raise_exception=True) AGREGAR A TODAS PERO PRIMERO HAY QUE CONFIGURAR ADMIN BIEN POR LOS PERMISOS
@login_required
def listarFacturas(request):
    query = request.GET.get('busquedaFactura', '').lower() 
    facturas = Factura.listarFacturas()
    estados_factura = EstadoFactura.objects.all()

    if query:
        facturas = [
            factura for factura in facturas
            if (
                query in str(factura['numero_comprobante']).lower() or
                factura['nombre_cliente'].lower().startswith(query) or
                factura['apellido_cliente'].lower().startswith(query) or
                factura['nombre_edificio'].lower().startswith(query)
            )
        ]

    context = paginacionTablas(request, facturas, 'facturas')
    context['estados_factura'] = estados_factura 
    
    return render(request, 'vistaFacturas.html', context)

@login_required
def generar_link_pago(request, id_factura):
    try:
        facturas = Factura.listarFacturas()
        vista_factura = None
        for factura in facturas:
            if factura['id_factura'] == id_factura:  
                vista_factura = factura
                break
        
        if not vista_factura:
            raise Http404("Factura no encontrada")
        
        nombre_cliente = vista_factura['nombre_cliente']
        apellido_cliente = vista_factura['apellido_cliente']
        descarga_ticket = vista_factura['descarga_ticket']
        
        # Obtén los detalles de los servicios y divide en listas
        detalles_servicios = vista_factura['detalles']
        
        items = []
        for detalle in detalles_servicios:
            nombres_servicios = detalle['nombre_servicio'].split(", ")
            cantidades_servicios = detalle['cantidad_servicio'].split(", ")
            precios_totales_servicios = detalle['precio_total_servicio'].split(", ")
            
            for nombre, cantidad, precio in zip(nombres_servicios, cantidades_servicios, precios_totales_servicios):
                items.append({
                    "title": nombre,
                    "quantity": 1,
                    "unit_price": float(precio),
                    "currency_id": "ARS"
                })

        # Configuración de Mercado Pago
        sdk = mercadopago.SDK("TEST-1083456035276298-101922-810a2e0aeb770bbf8ed3191b3cd59702-566328219")

        # Datos de la preferencia
        preference_data = {
            "items": items,
            "payer": {
                "email": vista_factura['detalles'][0]['correo_cliente']
            }
        }

        # Crear preferencia
        preference = sdk.preference().create(preference_data)
        payment_link = preference["response"].get("init_point")

        # Enviar correo con el link de pago
        Factura.enviar_correo_link_pago(
            vista_factura['detalles'][0]['correo_cliente'],
            payment_link,
            nombre_cliente,
            apellido_cliente,
            descarga_ticket
        )
        
        messages.success(request, f"El link de pago se envió correctamente. Link: {payment_link}")
        return redirect(reverse('facturas:listarFacturas'))
        
    except Exception as e:
        print(f"Error detallado: {str(e)}")
        messages.error(request, f"Ocurrió un error: {str(e)}")
        return redirect(reverse('facturas:listarFacturas'))

@login_required
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

        return redirect('/facturas/')

    return redirect('/facturas/')