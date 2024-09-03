from django.shortcuts import render
from .models import Actividades
from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required


@login_required
def listarActividades(request):
    if not request.user.is_authenticated:
        return HttpResponse("No autenticado")
    print('autenticado')
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

    #print(act_modificadas)
        
    return render(request, 'index.html', {'act_modificadas': act_modificadas})
    