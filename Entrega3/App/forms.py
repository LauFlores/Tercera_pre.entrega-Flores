from django import forms

class reservaFormulario(forms.Form):
    codigo_de_reserva=forms.CharField()
    fecha= forms.DateField()
    hora= forms.IntegerField()
 
class clubFormulario(forms.Form):
    codigo_de_reserva=forms.CharField()
    nombre= forms.CharField()
    email= forms.EmailField()
    num_cancha= forms.IntegerField()

class profesorFormulario(forms.Form):
    codigo_de_reserva=forms.CharField()
    nombre = forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()

class alumnoFormulario(forms.Form):
    codigo_de_reserva=forms.CharField()
    nombre= forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()
    tel= forms.IntegerField()


    

