"""
URL configuration for consortiumSolutions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicaciones.login.urls')),
    path('empleados/', include('Aplicaciones.empleados.urls', namespace='empleados')), 
    path('inicio/', include('Aplicaciones.inicio.urls', namespace='inicio')),  # Esta será la ruta que redirige a login # Esta será la ruta que redirige a login
    path('servicios/', include('Aplicaciones.servicios.urls', namespace='servicios')),
    path('clientes/', include('Aplicaciones.clientes.urls', namespace='clientes')),
    path('presupuestos/', include('Aplicaciones.presupuestos.urls', namespace='presupuestos')),
    path('ventas/', include('Aplicaciones.ventas.urls', namespace='ventas')),
    path("__reload__/", include("django_browser_reload.urls")),
]


