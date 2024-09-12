from django.urls import path
from . import views

app_name = 'presupuestos'
urlpatterns = [
    path('', views.home, name='home'),
    path('presupuesto/<int:id_presupuesto>/', views.detalle_presupuesto, name='detalle_presupuesto'),
    path('agregar/', views.agregarPresupuesto, name='agregarPresupuesto'),
]