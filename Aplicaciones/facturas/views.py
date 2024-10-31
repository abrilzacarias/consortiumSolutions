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
    facturas = Factura.listarFacturas()
    estados_factura = EstadoFactura.objects.all()
    print(facturas)

    
    # Pasar la lista `facturas` para paginación
    context = paginacionTablas(request, facturas, 'facturas')
    context['estados_factura'] = estados_factura 
    
    return render(request, 'vistaFacturas.html', context)
@login_required
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
        nombre_cliente = vista_factura[3]
        apellido_cliente= vista_factura[4]
        descarga_ticket = vista_factura[6]
        nombres_servicios = vista_factura[9].split(", ")  # 'Reparación de pisos, Limpieza de Vidrios'
        cantidades_servicios = vista_factura[10].split(", ")  # '1, 1'
        precios_totales_servicios = vista_factura[11].split(", ")  # '105, 85'
        correo_cliente = vista_factura[12]

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

        preference = sdk.preference().create(preference_data)
        payment_link = preference["response"].get("init_point")
        Factura.enviar_correo_link_pago(correo_cliente, payment_link, nombre_cliente, apellido_cliente, descarga_ticket)
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

        return redirect(reverse('facturas:listarFacturas'))

    return redirect(reverse('facturas:listarFacturas'))