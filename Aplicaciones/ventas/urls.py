from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('', views.home, name='home'),
    path('enviar_factura_prueba/<int:id_venta>/', views.enviar_factura_prueba, name='enviar_factura_prueba'),
    path('editarVenta/<int:id_venta>/', views.editarVenta, name='editarVenta'),
]