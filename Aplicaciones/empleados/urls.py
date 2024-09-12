from django.urls import path
from . import views

app_name = 'empleados'

urlpatterns = [
    path('', views.home, name='home'),
    path('agregarEmpleado/', views.agregarEmpleado, name='agregarEmpleado'),
    path('editarEmpleado/<int:id_empleado>/', views.editarEmpleado, name='editarEmpleado'),
    path('eliminarEmpleado/<int:id_empleado>/', views.eliminarEmpleado, name='eliminarEmpleado'),
    path('eliminarContactoEmpleado/<int:id_contacto>/', views.eliminarContactoEmpleado, name='eliminarContactoEmpleado'),
]