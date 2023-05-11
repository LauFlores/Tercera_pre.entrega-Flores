from django.urls import path
from App import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('reserva', views.reserva, name='reserva'),
    path('club', views.club, name="club"),
    path('profesor', views.profesor, name="profesor"),
    path('alumno', views.alumno, name="alumno"),
    path('buscar/',views.buscar,name="buscar"),
]