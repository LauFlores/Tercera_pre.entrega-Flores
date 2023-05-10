from django.shortcuts import render
from App.models import Club, Profesor, Alumno, Reserva
from django.http import HttpResponse
from App.forms import clubFormulario, profesorFormulario, alumnoFormulario, reservaFormulario

# Create your views here.
def inicio(request):
    return render(request, 'App/inicio.html')
def club(request):
    return render(request,'App/club.html')
def profesor(request):
    return render(request,'App/profesor.html')
def alumno(request):
    return render(request,'App/alumno.html')
def reserva(request):
    return render(request,'App/reserva.html')


def club(request):
    if request.method =='POST':
        miFormulario=clubFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            club=Club(
                codigo_de_reserva=informacion['codigo_de_reserva'],
                nombre=informacion['nombre'],
                email=informacion['email'],
                num_cancha=informacion['num_cancha'])
            club.save()
            return render(request, 'App/inicio.html')
    else:
        miFormulario=clubFormulario()
    return render(request, 'App/club.html', {"miFormulario": miFormulario})

def profesor(request):
     if request.method == "POST":
        miFormulario1 = profesorFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario1)
        
        if miFormulario1.is_valid:
            informacion = miFormulario1.cleaned_data
            profesor = Profesor(
                codigo_de_reserva= informacion['codigo_de_reserva'],
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'])
            profesor.save()
            return render(request, "App/inicio.html")
     else:
        miFormulario1 = profesorFormulario()
             
     return render(request, "App/profesor.html", {"miFormulario1": miFormulario1})

def alumno(request):
    if request.method =='POST':
        miFormulario2=alumnoFormulario(request.POST)
        print(miFormulario2)

        if miFormulario2.is_valid:
            informacion=miFormulario2.cleaned_data
            alumno=Alumno(
                codigo_de_reserva=informacion['codigo_de_reserva'],
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                tel=informacion['tel'])
            alumno.save()
            return render(request, 'App/inicio.html')
    else:
        miFormulario2=alumnoFormulario()
    return render(request, 'App/alumno.html', {"miFormulario2": miFormulario2})

def reserva(request):
    if request.method =='POST':
        miFormulario3=reservaFormulario(request.POST)
        print(miFormulario3)

        if miFormulario3.is_valid:
            informacion=miFormulario3.cleaned_data
            reserva=Reserva(
                codigo_de_reserva=informacion['codigo_de_reserva'],
                fecha=informacion['fecha'],
                hora=informacion['hora'])
            reserva.save()
            return render(request, 'App/inicio.html')
    else:
        miFormulario3=reservaFormulario()
    return render(request, 'App/reserva.html', {"miFormulario3": miFormulario3})

def buscarReserva(request):
     return render(request,'App/buscarReserva.html')

def buscar(request):
     if request.GET['codigo_de_reserva']:
          codigo_de_reserva = request.GET['codigo_de_reserva']
          reserva= reserva.objects.filter(codigo_de_reserva__icontains=codigo_de_reserva)

          return render(request,'App/resultadosBusqueda.html', {"reserva":reserva, "codigo_de_reserva": codigo_de_reserva })
     else:
          respuesta= "No enviaste datos"

     return HttpResponse(respuesta)


