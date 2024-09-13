from django.urls import path
from . import views

app_name = 'servicios'

urlpatterns = [
    path('', views.home, name='home'),
    path('agregarCategoria/', views.agregarCategoria, name='agregarCategoria'),
    path('agregarServicio/', views.agregarServicio, name='agregarServicio'),
    path('eliminarCategoria/<id_categoria>', views.eliminarCategoria, name='eliminarCategoria'),
    path('eliminarServicio/<id_servicio>', views.eliminarServicio, name='eliminarServicio'),
    path('editarServicio/<int:id_servicio>/', views.editarServicio, name='editarServicio'),
    path('buscarServicioOCategoria/', views.buscarServicioOCategoria, name='buscar_servicio_categoria'),
    path('aumentarPrecio/', views.aumentarPrecio, name='aumentarPrecio'),
]