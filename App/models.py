from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha = models.DateField(blank=True, null=True,)
    imagen = models.ImageField(upload_to="Blog_imagen/", blank=True)


class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"


