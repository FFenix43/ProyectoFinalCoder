from django.shortcuts import render
#from .models import 
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from LOTR.forms import SignupForm
from LOTR.models import Registro
# Create your views here.



def AboutMe(request):
    return render(request, "aboutme.html")

def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

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
                usuario=Registro(nombre=nom,apellido=ape,gmail=mail,contraseña=contrase,confirmar=confir)
                usuario.save()
                return render(request, "home.html")
            else:
                return render(request, "signup.html", {"mensaje": "deben coincidir las contraseñas"})

    else:
        formulario=SignupForm()
        return render(request, "signup.html", {"form":formulario})
    

def blogs(request):
    return render(request, "blogs.html")

def indice(request):
    return render(request, "indice.html")