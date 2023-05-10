from django.urls import path
from App import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('clubes', views.clubes, name="Clubes"),
    path('profesores', views.profesores, name="Profesores"),
    path('alumnos', views.alumnos, name="Alumnos"),
    path('reservas', views.reservas, name="Reservas"),
    path('buscarReserva',views.buscarReserva,name="BuscarReserva"),
    path('buscar/',views.buscar),
]