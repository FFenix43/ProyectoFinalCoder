from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class CreacionUsario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields} #para cada uno de los campos del formulario le asigna un valor vacio

class EditorDeUsuario(UserCreationForm):
    email=forms.EmailField()
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Modificar el nombre")
    last_name=forms.CharField(label="Modificar Apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields} #para cada uno de los campos del formulario le asigna un valor vacio

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="imagen")


class FormsCrearBlogs(forms.Form):
    nombre_personaje=forms.CharField(max_length=20)
    imagen=forms.ImageField(label="imagen")
    parrafo=forms.CharField(widget=forms.Textarea)

class mensaje(forms.Form):
    mensaje=forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User