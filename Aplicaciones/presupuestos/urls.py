from django.urls import path
from . import views

app_name = 'presupuestos'
urlpatterns = [
    path('', views.home, name='home'),
    path('presupuesto/<int:id_presupuesto>/', views.detalle_presupuesto, name='detalle_presupuesto'),
    path('agregarPresupuesto/', views.agregarPresupuesto, name='agregarPresupuesto'),
    path('vendedores/', views.mostrar_vendedores, name='vendedores'),
    path('servicios/', views.mostrar_servicios, name='servicios'),
    path('eliminarPresupuesto/<int:id_presupuesto>/', views.eliminarPresupuesto, name='eliminarPresupuesto'),
]