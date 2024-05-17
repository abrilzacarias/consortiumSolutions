from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('agregarCategoria/', views.agregarCategoria),
    path('agregarServicio/', views.agregarServicio),
    path('eliminarCategoria/<id_categoria>', views.eliminarCategoria),
    path('eliminarServicio/<id_servicio>', views.eliminarServicio),
    path('editarServicio/<int:id_servicio>/', views.editarServicio, name='editar_servicio'),
    path('buscarServicioOCategoria/', views.buscarServicioOCategoria, name='buscar_servicio_categoria'),
]