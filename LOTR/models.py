from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class blogs(models.Model):
    
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    gmail=models.EmailField()
    contraseña=models.CharField(max_length=8)

   

    def __str__(self) -> str:
        return self.nombre+" "+self.apellido+" "+self.gmail+" "+self.contraseña


class Avatar(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self) -> str:
        return f"{self.user} - {self.imagen}"