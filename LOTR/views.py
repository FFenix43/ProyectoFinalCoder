from django.shortcuts import render
#from .models import 
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from LOTR.forms import SignupForm, LoginForm
from LOTR.models import Registro

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def AboutMe(request):
    return render(request, "aboutme.html")
@login_required
def home(request):
    return render(request, "home.html")

def login(request):
    if request.method=="POST":
        formulario=LoginForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            mail=informacion["mail"]
            contrase=informacion["contra"]
            return render(request, "home.html", {"nombre": mail})
            
                

    else:
        formulario=LoginForm()
        return render(request, "login.html", {"form":formulario})
        


def signup(request):
    
    if request.method=="POST":
        formulario=SignupForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            nom=informacion["nombre"]
            ape=informacion["apellido"]
            mail=informacion["gmail"]
            contrase=informacion["contra"]
            confir=informacion["confirmar"]
            if contrase==confir:
                usuario=Registro(nombre=nom,apellido=ape,gmail=mail,contraseña=contrase)
                usuario.save()
                return render(request, "home.html", {"mensaje": "Suscripcion exitosa!", "nombre": nom})
            else:
                return render(request, "signup.html", {"mensaje": "deben coincidir las contraseñas"})

    else:
        formulario=SignupForm()
        return render(request, "signup.html", {"form":formulario})
    
@login_required
def blogs(request):
    return render(request, "blogs.html")
@login_required
def indice(request):
    return render(request, "indice.html")