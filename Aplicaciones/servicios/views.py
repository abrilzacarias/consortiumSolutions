from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import CategoriaServicio, Servicio
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages
from django.forms.models import model_to_dict

def home(request):
    categorias = CategoriaServicio.objects.all()

    servicios = Servicio.objects.all()

    print(servicios.count())

    for servicio in servicios:
        servicio_dict = model_to_dict(servicio)
        for field, value in servicio_dict.items():
            print(f"{field}: {value}")
    return render(request, 'serviciosviews.html', {'categorias': categorias, 'servicios': servicios})

def agregarCategoria(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria')  
        if categoria:  
            CategoriaServicio.agregarCategoria(categoria)  
    return redirect(reverse('servicios:home'))  

def agregarServicio(request):
    if request.method == 'POST':
        nombre_servicio = request.POST.get('nombre_servicio')
        requiere_pago = request.POST.get('requiere_pago') == '1'  
        precio_base = request.POST.get('precio_base')
        categoria_id = request.POST.get('categoria_id')  
        categoria_servicio = get_object_or_404(CategoriaServicio, pk=categoria_id)
        Servicio.objects.create(nombre_servicio=nombre_servicio, requiere_pago_servicio=requiere_pago, precio_base_servicio=precio_base,id_categoria_servicio=categoria_servicio)
    return redirect(reverse('servicios:home'))

def aumentarPrecio(request):
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria')
        porcentaje_aumento = request.POST.get('porcentaje_aumento')
        
        categoria = CategoriaServicio.objects.get(id_categoria_servicio=categoria_id)
        if categoria.aumentarPrecio(categoria_id, porcentaje_aumento):
            messages.success(request, 'El precio se ha aumentado exitosamente.')
            return redirect('/servicios/')  
        else:
            messages.error(request, 'No se pudo aumentar el precio.')
    return redirect('/servicios/')

def eliminarCategoria(request, id_categoria):
    categoria = CategoriaServicio.objects.get(id_categoria_servicio=id_categoria)
    Servicio.objects.filter(id_categoria_servicio=id_categoria).delete()
    categoria.delete()

    return redirect(reverse('servicios:home'))

def eliminarServicio(request, id_servicio):
    servicio = Servicio.objects.get(id_servicio=id_servicio)
    servicio.delete()

    return redirect(reverse('servicios:home'))

def editarServicio(request, id_servicio):
    if request.method == 'POST':
        nombre_servicio = request.POST.get('nombre_servicio')
        requiere_pago = request.POST.get('requiere_pago_editar') == '1' 
        precio_base = request.POST.get('precio_base')
        categoria_id = request.POST.get('categoria_servicio')
        categoria_servicio = get_object_or_404(CategoriaServicio, pk=categoria_id)
        
        if not requiere_pago:
            precio_base = None
        
        servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
        servicio.nombre_servicio = nombre_servicio
        servicio.requiere_pago_servicio = requiere_pago
        servicio.precio_base_servicio = precio_base
        servicio.id_categoria_servicio = categoria_servicio  
    
        servicio.save()
        return redirect(reverse('servicios:home'))

    
def buscarServicioOCategoria(request):
    resultadosServicios = []
    resultadosCategorias = []
    busqueda = request.GET.get('buscar')
    if busqueda:
        resultadosServicios = Servicio.objects.filter(nombre_servicio__icontains=busqueda)
        resultadosCategorias = CategoriaServicio.objects.filter(nombre_categoria_servicio__icontains=busqueda)
    return render(request, 'serviciosviews.html', {'serviciosBusqueda': resultadosServicios, 'categoriasBusqueda': resultadosCategorias, 'query': busqueda})


