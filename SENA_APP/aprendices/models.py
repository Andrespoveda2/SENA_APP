from django.db import models

class Aprendiz(models.Model):
  documento_identidad = models.CharField(max_length=255, unique=True)
  nombre = models.CharField(max_length=255)
  apellido = models.CharField(max_length=255)
  telefono = models.IntegerField(null=True)
  correo = models.EmailField(null=True)
  Fecha_nacimiento = models.DateField(null=True)
  ciudad = models.CharField(max_length=255)
  programa = models.CharField(max_length=255)
  
  def __str__(self):
    return f"{self.nombre} {self.apellido} - {self.documento_identidad}"
# Create your models here.
