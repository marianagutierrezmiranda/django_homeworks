from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    
    context = {}
    
    if request.method == 'POST':
        request.session['nombre'] = request.POST.get("nombre")
        request.session.set_expiry(request.session.get_session_cookie_age())
        request.session['expiry_age'] = request.session.get_expiry_age()
        context['nombre'] = request.session['nombre']
        context["expiry_age"] = request.session['expiry_age'] / 60
        context["expiry_date"] = request.session.get_expiry_date()
    
    if request.method == 'GET' and 'nombre' in request.session:
        context['nombre'] = request.session['nombre']
        context["expiry_age"] = request.session['expiry_age']
        context["expiry_date"] = request.session.get_expiry_date()
        
    return render(request, 'cookies_website/index.html', context)
