from django.shortcuts import render, redirect
from .models import CategoriaServicio, Servicio
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    categorias = CategoriaServicio.objects.all()
    servicios = Servicio.objects.all()
    
    return render(request, 'serviciosviews.html', {'categorias': categorias, 'servicios': servicios})

def agregarCategoria(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria')  # Obtener el valor del campo 'categoria' del formulario
        if categoria:  # Verificar si se recibió un valor para 'categoria'
            CategoriaServicio.agregarCategoria(categoria)  # Crear la nueva categoría
    return redirect('/')  # Redirigir al usuario a la página principal (home)

def agregarServicio(request):
    if request.method == 'POST':
        nombre_servicio = request.POST.get('nombre_servicio')
        requiere_pago = request.POST.get('requiere_pago') == '1'  # Convertir el valor del dropdown a un booleano
        categoria_id = request.POST.get('categoria_id')  # Obtener el ID de la categoría seleccionada
        categoria_servicio = get_object_or_404(CategoriaServicio, pk=categoria_id)
        # Aquí puedes crear el servicio usando los datos proporcionados
        Servicio.objects.create(nombre_servicio=nombre_servicio, requiere_pago_servicio=requiere_pago, id_categoria_servicio=categoria_servicio)
        
        # Redireccionar a alguna página después de agregar el servicio
    return redirect('/')

def eliminarCategoria(request, id_categoria):
    categoria = CategoriaServicio.objects.get(id_categoria_servicio=id_categoria)
    Servicio.objects.filter(id_categoria_servicio=id_categoria).delete()
    categoria.delete()

    return redirect('/')

def eliminarServicio(request, id_servicio):
    servicio = Servicio.objects.get(id_servicio=id_servicio)
    servicio.delete()

    return redirect('/')

def editarServicio(request, id_servicio):
    if request.method == 'POST':
        print(id_servicio)
        nombre_servicio = request.POST.get('nombre_servicio')
        requiere_pago = request.POST.get('requiere_pago') == '1'
        categoria_id = request.POST.get('categoria_servicio')
        categoria_servicio = get_object_or_404(CategoriaServicio, pk=categoria_id)
        
        servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
        servicio.nombre_servicio = nombre_servicio
        servicio.requiere_pago_servicio = requiere_pago
        servicio.id_categoria_servicio = categoria_servicio  # Actualiza la categoría
    
        servicio.save()
        
        return redirect('/')
    
def buscarServicioOCategoria(request):
    resultadosServicios = []
    resultadosCategorias = []
    busqueda = request.GET.get('buscar')
    if busqueda:
        resultadosServicios = Servicio.objects.filter(nombre_servicio__icontains=busqueda)
        resultadosCategorias = CategoriaServicio.objects.filter(nombre_categoria_servicio__icontains=busqueda)
    return render(request, 'serviciosviews.html', {'serviciosBusqueda': resultadosServicios, 'categoriasBusqueda': resultadosCategorias, 'query': busqueda})


