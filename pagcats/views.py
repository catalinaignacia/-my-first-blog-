from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def post_list(request):
    return render(request, 'pagcats/home.html', {})

def post_web2(request):
    return render(request, 'pagcats/formulario_mascota.html', {})

def post_web3(request):
    return render(request, 'pagcats/contacto.html', {})

