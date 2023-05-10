from django import forms
 
class ClubFormulario(forms.Form):
    Id_club=forms.IntegerField()
    nombre= forms.CharField()
    email= forms.EmailField()

class ProfesorFormulario(forms.Form):
    Id_profesor = forms.IntegerField()
    nombre = forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()


class AlumnoFormulario(forms.Form):
    Id_alumno=forms.IntegerField()
    nombre= forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()
    tel= forms.IntegerField()

class ReservaFormulario(forms.Form):
    Id_reserva=forms.IntegerField()
    fecha= forms.DateField()
    hora= forms.DateTimeField()
    Id_profesor= forms.IntegerField()
    Id_club= forms.IntegerField()
    Id_alumno= forms.IntegerField()
    num_cancha= forms.IntegerField()

