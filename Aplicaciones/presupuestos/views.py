from django.shortcuts import render
from .models import Presupuesto

# Create your views here.
def home(request):
    
    print('hola llego al def home')
    presupuestos = Presupuesto.objects.all()
    print(presupuestos)
    return render(request, 'listarPresupuestos.html', {'presupuestos': presupuestos})
