from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class blogs(models.Model):
    
    nombre_del_personaje=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='Fotos-Blogs', default='C:\TOMAS AGOSTINO ALVARENGA\CODER-HOUSE\ProyectoFinal\media\avatares\avatarDefault.jpg')
    parrafo=models.TextField(max_length=5000, default=None)
    

   

    def __str__(self) -> str:
        return f"{self.nombre_del_personaje} - {self.imagen} - {self.parrafo}"


class Avatar(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.user} - {self.imagen}"


class Mensajes(models.Model):
    mensaje=models.TextField()
    
    def __str__(self) -> str:
        return f"{self.mensaje}"