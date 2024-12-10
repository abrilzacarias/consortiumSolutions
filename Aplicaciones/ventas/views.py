from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import MetodoPago, Venta, EstadoVenta, RegistroEstadoVenta, DetalleVenta  # Asegúrate de importar la clase MetodoPago
from django.contrib import messages
from ..facturas.models import Factura
from ..inicio.views import paginacionTablas
import http.client, json
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required

#TODO @permission_required('inicio.view_detalleventa', login_url='', raise_exception=True) AGREGAR A TODAS PERO PRIMERO HAY QUE CONFIGURAR ADMIN BIEN
@login_required
def home(request):
    query = request.GET.get('busquedaVenta', '').lower()  
    ventas = Venta.listarVentas()
    metodos_pago = MetodoPago.obtenerMetodosPago() # Asegúrate de incluir esto
    estados_venta = EstadoVenta.obtenerEstadosVenta()

    if query:
        ventas = [
            venta for venta in ventas
            if venta['numero_factura'].lower().startswith(query) or
               venta['nombre_empleado'].lower().startswith(query) or
               venta['nombre_edificio'].lower().startswith(query)
        ]

    context = paginacionTablas(request, ventas, 'ventas')
    context['metodos_pago'] = metodos_pago  # Agrega métodos de pago al contexto
    context['estados_venta'] = estados_venta
    #context['detalles'] = detalle_venta_queryset  # Asegúrate de que incluye el id_estado_venta
    return render(request, 'ventasViews.html', context)


@login_required
def enviar_facturacion(request, id_venta):
    print(f"ID venta recibido en enviar facturacion: {id_venta}")  # Imprimir el id_venta
    id_factura = Venta.enviar_facturacion(id_venta)
    if id_factura:
        print(f"Venta creada con ID: {id_factura}")  # Imprimir el id de la factura creada
        messages.success(request, 'El presupuesto se ha transferido a ventas exitosamente.')
        return redirect('/ventas/')
    else:
        print("Error al crear la factura.")  # Imprimir mensaje de error
        return redirect('/ventas/')  


@login_required
def editarMetodoPago(request, id_venta):
    if request.method == 'POST':
        try:
            # Imprimir todos los datos que llegan en el POST
            print(request.POST)  # Esto te mostrará todos los datos enviados por el formulario

            # Obtener el nuevo método de pago del formulario
            id_nuevo_metodo_pago = request.POST.get('metodo_pago')

            # Llama al método de clase para actualizar el método de pago
            actualizado = Venta.actualizarMetodoPago(id_nuevo_metodo_pago, id_venta)

            if actualizado:
                # Mensaje de éxito si la actualización fue correcta
                messages.success(request, 'El método de pago se actualizó correctamente.')
            else:
                # Mensaje de error si la actualización falló
                messages.error(request, 'Hubo un error al actualizar el método de pago.')

        except Exception as e:
            # Capturar excepciones inesperadas y notificar al usuario
            messages.error(request, f'Hubo un problema al actualizar el método de pago: {str(e)}')

        # Redirige a la vista principal de ventas
        return redirect('ventas:home')

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


@login_required
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

@login_required
def agregarObservacionDetalleVenta(request, id_detalle_venta):
    if request.method == 'POST':
        descripcion_observacion = request.POST.get('descripcion_observacion')
        id_empleado = request.user.id_usuario  # Cambia a id_usuario
        DetalleVenta.agregarObservacionDetalleVenta(id_detalle_venta, descripcion_observacion, id_empleado)
    return redirect('/ventas/')
