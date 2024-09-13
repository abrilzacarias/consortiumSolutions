from django.urls import path
from . import views

app_name = 'presupuestos'
urlpatterns = [
    path('', views.home, name='home'),
    path('presupuesto/<int:id_presupuesto>/', views.detalle_presupuesto, name='detalle_presupuesto'),
    path('agregarPresupuesto/', views.agregarPresupuesto, name='agregarPresupuesto'),
    path('vendedores/', views.mostrar_vendedores, name='vendedores'),
    path('clientes/', views.mostrar_clientes, name='clientes'),
    path('edificios/<int:id_cliente>/', views.mostrar_edificios, name='edificios'),
    path('servicios/', views.obtener_servicios, name='obtener_servicios'),
]