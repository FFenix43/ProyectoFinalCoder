from django.db import models

# Create your models here.

class Registro(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    gmail=models.EmailField()
    contraseña=models.CharField(max_length=8)
   

    def __str__(self) -> str:
        return self.nombre+" "+self.apellido+" "+self.gmail+" "+self.contraseña

