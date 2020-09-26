from django.shortcuts import render
from .models import ListaDeDistribucion


def index(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'blog/index.html', context)

def page2(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'blog/page2.html', context)

def article(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'blog/article.html', context)

def about(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'blog/about.html', context)
        
def emails(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'blog/emails.html', context)
    if request.method == 'POST':
        cliente = ListaDeDistribucion.objects.create(email = request.POST.get("email"))
        cliente.save()
        context["msg"] = 'Tu email fue agregado exitosamente'
        context["emails"] = ListaDeDistribucion.objects.all()
        return render(request, 'blog/emails.html', context)

