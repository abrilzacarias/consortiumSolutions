from django.urls import path
from . import views

app_name = 'vendedores'

urlpatterns = [
    path('', views.home, name='home'),
    path('agregarVendedor/', views.agregarVendedor, name='agregarVendedor'),
    path('editarVendedor/<int:id_vendedor>/', views.editarVendedor, name='editarVendedor'),
    path('eliminarVendedor/<int:id_vendedor>/', views.eliminarVendedor, name='eliminarVendedor'),
    path('eliminarContacto/<int:id_contacto>/', views.eliminarContacto, name='eliminarContacto'),
]