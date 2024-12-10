from django.urls import path
from . import views

app_name =  'facturas'
urlpatterns = [
    path('', views.listarFacturas, name='listarFacturas'),
    path('actualizar_estado_factura/<int:id_factura>/', views.actualizar_estado_factura, name='actualizar_estado_factura'),
   
]