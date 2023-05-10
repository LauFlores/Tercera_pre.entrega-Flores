from django.shortcuts import render
from App.models import Club, Profesor, Alumno, Reserva
from django.http import HttpResponse
from App.forms import ClubFormulario, ProfesorFormulario, AlumnoFormulario, ReservaFormulario

# Create your views here.
def inicio(request):
    return render(request, 'App/inicio.html')
def clubes(request):
    return render(request,'App/clubes.html')
def profesores(request):
    return render(request,'App/profesores.html')
def alumnos(request):
    return render(request,'App/alumnos.html')
def reservas(request):
    return render(request,'App/reservas.html')


def clubes(request):
    if request.method =='POST':
        miFormulario=ClubFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            club=Club(int(informacion['Id_club']),str(informacion['nombre']),informacion['email'])
            club.save()
            return render(request, 'App/inicio.html')
    else:
        miFormulario=ClubFormulario()
    return render(request, 'App/clubes.html', {"miFormulario": miFormulario})

def profesores(request):
     if request.method == "POST":
        miFormulario1 = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario1)
        
        if miFormulario1.is_valid:
            informacion = miFormulario1.cleaned_data
            profesor = Profesor(int(informacion['Id_profesor']),str(informacion['nombre'],informacion['apellido'],
                                   informacion['email']))
            profesor.save()
            return render(request, "App/inicio.html")
     else:
        miFormulario1 = ProfesorFormulario()
             
     return render(request, "App/profesores.html", {"miFormulario1": miFormulario1})

def alumnos(request):
    if request.method =='POST':
        miFormulario2=AlumnoFormulario(request.POST)
        print(miFormulario2)

        if miFormulario2.is_valid:
            informacion=miFormulario2.cleaned_data
            alumno=Alumno(int(informacion['Id_profesor']),str(informacion['nombre'],informacion['apellido'],
                                   informacion['email']),int(informacion['tel']))
            alumno.save()
            return render(request, 'App/inicio.html')
    else:
        miFormulario2=AlumnoFormulario()
    return render(request, 'App/alumnos.html', {"miFormulario2": miFormulario2})

def reservas(request):
    if request.method =='POST':
        miFormulario3=ReservaFormulario(request.POST)
        print(miFormulario3)

        if miFormulario3.is_valid:
            informacion=miFormulario3.cleaned_data
            reserva=Reserva(int(informacion['Id_reserva'],informacion['fecha'],informacion['hora'],
                                   informacion['Id_profesor'],informacion['Id_club'],informacion['Id_alumno'],informacion['num_cancha']))
            reserva.save()
            return render(request, 'App/inicio.html')
    else:
        miFormulario3=ReservaFormulario()
    return render(request, 'App/reservas.html', {"miFormulario3": miFormulario3})

def buscarReserva(request):
     return render(request,'App/buscarReserva.html')

def buscar(request):
     if request.GET['curso']:
          club = request.GET['curso']
          clubes= club.objects.filter(curso__icontains=club)

          return render(request,'App/resultadosBusqueda.html', {"cursos":clubes, "comisiones": club })
     else:
          respuesta= "No enviaste datos"

     return HttpResponse(respuesta)


