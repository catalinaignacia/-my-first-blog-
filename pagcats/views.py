from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    return render(request, 'pagcats/home.html')

def post_web2(request):
    return render(request, 'pagcats/formulario_mascota.html')

def post_web3(request):
    return render(request, 'pagcats/contacto.html')

def post_register(request):
    if request.method == "Post":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'cuentas/registrar.html',{'form':form})