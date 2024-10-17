from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('', views.home, name='home'),
    path('factura-prueba/', views.enviar_factura_prueba, name='factura-prueba')
]