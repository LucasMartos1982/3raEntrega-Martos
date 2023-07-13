from django.db import models

# Create your models here.

class Estudiantes (models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()

class Curso(models.Model):
    nombre=models.CharField(max_length=20)
    camada=models.IntegerField()
     
class Profesor(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()
    profesion=models.CharField(max_length=20)
    
class Entregables (models.Model):
    nombre=models.CharField(max_length=20)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()