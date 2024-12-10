from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('', views.home, name='home'),
    path('enviar_facturacion/<int:id_venta>/', views.enviar_facturacion, name='enviar_facturacion'),
    path('editarMetodoPago/<int:id_venta>/', views.editarMetodoPago, name='editarMetodoPago'),
    path('cambiarEstadoRegistroVenta/<int:id_detalle_venta>/', views.cambiarEstadoRegistroVenta, name='cambiarEstadoRegistroVenta'),
    path('agregarObservacionDetalleVenta/<int:id_detalle_venta>/', views.agregarObservacionDetalleVenta, name='agregarObservacionDetalleVenta'),
]
