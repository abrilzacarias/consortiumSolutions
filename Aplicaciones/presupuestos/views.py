from django.shortcuts import render

# Create your views here.
def home(request):
    
    print('hola llego al def home')
    return render(request, 'listarPresupuestos.html')
