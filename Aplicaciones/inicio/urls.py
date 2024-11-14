from django.urls import path
from . import views

app_name = 'inicio'
urlpatterns = [
    path('', views.listarActividades, name='listarActividades'),
]
