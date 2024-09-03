from django.urls import path
from . import views

app_name = 'presupuestos'
urlpatterns = [
    path('', views.home, name='home'),
]