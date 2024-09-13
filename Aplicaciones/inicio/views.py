from django.shortcuts import render
from .models import Actividades
from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required
def listarActividades(request):
    # Son registros de mentirita para probar.
    act_modificadas = [
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Alta Vendedor', 'descripcion_actividad': 'Se registró un nuevo vendedor.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Baja Cliente', 'descripcion_actividad': 'Un cliente fue dado de baja.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Observación', 'descripcion_actividad': 'Se agregó una observación a la cuenta de Mari.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Alta Cliente', 'descripcion_actividad': 'Nuevo cliente registrado.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Observación', 'descripcion_actividad': 'Se agregó una observación al presupuesto de Ezequiel.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Alta Cliente', 'descripcion_actividad': 'Nuevo cliente registrado.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Baja Vendedor', 'descripcion_actividad': 'Un vendedor fue dado de baja.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Alta Vendedor', 'descripcion_actividad': 'Se registró un nuevo vendedor.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Observación', 'descripcion_actividad': 'Se agregó una observación a la venta de Aldo.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Alta Cliente', 'descripcion_actividad': 'Nuevo cliente registrado.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Observación', 'descripcion_actividad': 'Se agregó una observación a la cuenta de un Abril.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Baja Cliente', 'descripcion_actividad': 'Un cliente fue dado de baja.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Alta Vendedor', 'descripcion_actividad': 'Se registró un nuevo vendedor.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Observación', 'descripcion_actividad': 'Se agregó una observación a la cuenta de un Brenda.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Alta Cliente', 'descripcion_actividad': 'Nuevo cliente registrado.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Alta Vendedor', 'descripcion_actividad': 'Se registró un nuevo vendedor.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Observación', 'descripcion_actividad': 'Se agregó una observación al presupuesto de Rels B.'},
        {'fecha_actividad': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'tipo_actividad': 'Baja Cliente', 'descripcion_actividad': 'Un cliente fue dado de baja.'},
    ]

    context = {
        'act_modificadas': act_modificadas
    }

    return render(request, 'index.html', context)

    