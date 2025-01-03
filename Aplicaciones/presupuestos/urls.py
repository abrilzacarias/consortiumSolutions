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
    path('eliminarPresupuesto/<int:id_presupuesto>/', views.eliminarPresupuesto, name='eliminarPresupuesto'),
    path('editarPresupuesto/', views.editarPresupuesto, name='editarPresupuesto'),
    path('obtenerPresupuesto/<int:id_presupuesto>/', views.obtenerPresupuesto, name='obtenerPresupuesto'),
    path('enviarVentas/<int:id_presupuesto>/', views.enviarVentas, name='enviarVentas'),
    path('eliminar_detalle/<int:id_detalle>/', views.eliminarDetallePresupuesto, name='eliminarDetallePresupuesto'),
    path('agregarObservacionPresupuesto/<int:id_detalle_presupuesto>/', views.agregarObservacionPresupuesto, name='agregarObservacionPresupuesto'),
]