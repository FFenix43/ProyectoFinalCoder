from django.shortcuts import render
#from .models import 
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from LOTR.forms import BlogsForm, CreacionUsario, EditorDeUsuario
from LOTR.models import blogs, Avatar
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases
from django.contrib.auth.decorators import login_required #para vistas basadas en vistas
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=user, password=clave)         #trae un usuario de la base y los compara y si existen los trae sino no trae nada
            if usuario is not None:
                login(request, usuario)
                return render(request, "home.html", {"mensaje": f"Bienvenido {user}"})
            else:
                return render(request, "Registro/login.html", {"mensaje": "Usuario o contraseña incorrecta"})
        else:
            return render(request, "Registro/login.html", {"mensaje":"Usuario o contraseña incorrecta", "form":form})
    else:
        form = AuthenticationForm()
        return render(request, "Registro/login.html", {"form": form})

def signup_request(request):
    if request.method == "POST":
        form=CreacionUsario(request.POST)
        
        if form.is_valid():
            clave=form.cleaned_data.get("password")
            user=form.cleaned_data.get("username")
            form.save()
            usuario=authenticate(username=user, password=clave)
            login(request, usuario)
            return render(request, "home.html", {"mensaje": f"Usuario {user} creado correctamente"})
        else:
            return render(request, "Registro/signup.html", {"mensaje": "Error al crear el usuario", "form": form })

    else:
        form=CreacionUsario()
    return render(request, "Registro/signup.html", {"form":form})


@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=EditorDeUsuario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "home.html", {"mensaje":"Perfil editado correctamente"})
        else:
            return render(request, "Regsitro/EditarUsuario.html", {"form":form, "nombreusuario":usuario.username, "mensaje":"Error al editar perfil"})

    else:
        form=EditorDeUsuario(instance=usuario)
        return render(request, "Registro/EditarUsuario.html", {"form":form, "nombreusuario":usuario.username})


    


@login_required
def AboutMe(request):
    return render(request, "aboutme.html")
@login_required
def home(request):
    nombre=request.user
    Nombre=nombre.username
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/avatarDefault.jpg"

    return render(request, "home.html", {"imagen":imagen, "nombre":Nombre})

@login_required
def CrearBlog(request):
    return HttpResponse("holamundo")

@login_required  
def BuscarBlogs(request):
    return render(request, "BuscarBlogs")