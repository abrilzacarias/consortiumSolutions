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