from django.db import models

# Create your models here.
class Club(models.Model):
    Id_club=models.IntegerField('idclub')
    nombre= models.CharField(max_length=40)
    email= models.EmailField()
    

class Alumno(models.Model):
    Id_alumno=models.IntegerField('idalumno')
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    tel= models.IntegerField()

class Profesor(models.Model):
    Id_profesor = models.IntegerField('idprofesor')
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    

class Reserva(models.Model):
    Id_reserva=models.IntegerField('idreserva')
    fecha= models.DateField()
    hora= models.DateTimeField()
    Id_profesor= models.CharField('idprofesor', max_length=50)
    Id_club= models.CharField('idclub', max_length=50)
    Id_alumno= models.CharField('idalumno', max_length=50)    
    num_cancha= models.IntegerField()