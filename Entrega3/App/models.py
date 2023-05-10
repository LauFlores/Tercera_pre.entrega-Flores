from django.db import models

class Reserva(models.Model):
    codigo_de_reserva=models.CharField(max_length=40)
    fecha= models.DateField()
    hora= models.IntegerField()

# Create your models here.
class Club(models.Model):
    codigo_de_reserva=models.CharField(max_length=40)
    nombre= models.CharField(max_length=40)
    email= models.EmailField()
    num_cancha= models.IntegerField()

class Profesor(models.Model):
    codigo_de_reserva=models.CharField(max_length=40)
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Alumno(models.Model):
    codigo_de_reserva=models.CharField(max_length=40)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    tel= models.IntegerField()


    


    