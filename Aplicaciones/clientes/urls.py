from django.urls import path
from . import views

app_name =  'clientes'
urlpatterns = [
    path('', views.listarClientes, name='listarClientes'),
    path('agregarCliente/', views.agregarCliente, name='agregarCliente'),
    path('editarCliente/<int:id_cliente>/', views.editarCliente, name='editarCliente'),
    path('eliminarCliente/<int:id_cliente>/', views.eliminarCliente, name='eliminarCliente'),
    path('agregarEdificio/<int:id_cliente>/', views.agregarEdificio, name='agregarEdificio'),
    path('agregarDesignacionVendedor/<int:id_cliente>/', views.agregarDesignacionVendedor, name='agregarDesignacionVendedor'),  
    path('agregarObservacionCliente/<int:id_cliente>/', views.agregarObservacionCliente, name='agregarObservacionCliente'),
    path('eliminarContactoCliente/<int:id_contacto>/', views.eliminarContactoCliente, name='eliminarContactoCliente'),
    path('eliminarEdificio/<int:id_edificio>/', views.eliminarEdificio, name='eliminarEdificio'),
    path('editarEdificio/<int:id_edificio>/', views.editarEdificio, name='editarEdificio'),
]