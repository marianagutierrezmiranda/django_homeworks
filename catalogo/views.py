from django.shortcuts import render
from .models import Productos, Clientes


def index(request):

    context = {}
    context['clientes'] = Clientes.objects.all()
    context['productos'] = Productos.objects.all()
    
    if request.method == 'GET':
                
        return render(request, 'catalogo/index.html', context)
        
    if request.method == 'POST':
        
        cliente = Clientes.objects.create(nombre = request.POST.get("nombre_cliente"))
        cliente.save()
        
        producto = Productos.objects.create(nombre = request.POST.get("nombre_producto"))
        producto.save()
        
        return render(request, 'catalogo/index.html', context)


def busqueda(request):

    context = {}
    
    if request.method == 'GET':
        return render(request, 'catalogo/busqueda.html', context)
        
    if request.method == 'POST':
        context['resultados'] = Productos.objects.filter(nombre__icontains=request.POST.get("nombre_producto"))
        return render(request, 'catalogo/busqueda.html', context)


def eliminar_cliente(request):

    context = {}
    
    if request.method == 'GET':
        context['clientes'] = Clientes.objects.all()
        return render(request, 'catalogo/eliminar_cliente.html', context)
        
    if request.method == 'POST':
        cliente = Clientes.objects.get(nombre = request.POST.get("nombre_cliente")) 
        cliente.delete()
        context['clientes'] = Clientes.objects.all()
        return render(request, 'catalogo/eliminar_cliente.html', context)
