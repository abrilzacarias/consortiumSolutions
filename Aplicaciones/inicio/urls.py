from django.urls import path, include
from . import views

app_name = 'inicio'
urlpatterns = [
    path('', views.listarActividades, name='listarActividades'),
]