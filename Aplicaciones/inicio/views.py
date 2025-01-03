import json
from django.shortcuts import render
from .models import Actividades, Graficos
from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.paginator import Paginator
from Aplicaciones.empleados.models import Empleado, TipoEmpleado


def paginacionTablas(request, datos, nombre_variable, items_por_pagina=10):
    paginator = Paginator(datos, items_por_pagina)
    page = request.GET.get('page') or 1
    paginated_data = paginator.get_page(page)
    
    context = {
        'datos': paginated_data,
        nombre_variable: paginated_data,
        'pagina_actual': int(page),
        'paginas': range(1, paginated_data.paginator.num_pages + 1)
    }

    return context
    
@login_required
def listarActividades(request):
    actividades = Actividades()
    listaActividades = actividades.listarActividades()
    act_modificadas = []
    for actividad in listaActividades:
        act_modificada = {
            'id_actividad' : actividad[0], 
            'tipo_actividad' : actividad[1],
            'descripcion_actividad' : actividad[2], 
            'fecha_actividad': actividad[3]
        }
        act_modificadas.append(act_modificada)
    
    datos_servicios = Graficos().serviciosMasVendidos()
    datos_cliente = Graficos().clienteMasCompras()
    # Crear diccionario de datos para el contexto
    graficos_data = {
        "servicios_mas_vendidos": datos_servicios,
        'cliente_mas_compras': datos_cliente
    }
    
    context = paginacionTablas(request, act_modificadas, nombre_variable='act_modificadas')
    context['graficos_data'] = json.dumps(graficos_data)
    print(graficos_data)
   
    return render(request, 'index.html', context)

def mostrarPerfil(request):
    usuario = request.user
    roles = usuario.groups.all()  

    print(f"Roles del usuario: {roles}")
    print(f"Usuario: {usuario}")

    return render(request, 'perfil.html', {
        'usuario': usuario,
        'roles': roles,
    })

    