from django.urls import path
from .views import inicio, jugadores, entrenadores, logros, nuevosjugadores, buscarjugador, nuevosentrenadores, buscarentrenador, nuevoslogros, buscarlogro  

urlpatterns = [
    path('', inicio, name="Inicio"),
    path("jugadores/", jugadores, name="Jugadores"),
    path("entrenadores/", entrenadores, name="Entrenadores"),
    path("logros/", logros, name="Logros"),
    path("nuevosjugadores/", nuevosjugadores, name="NuevosJugadores"),
    path("buscarjugador/", buscarjugador, name="BuscarJugador"),
    path("nuevosentrenadores/", nuevosentrenadores, name="NuevosEntrenadores"),
    path("buscarentrenador/", buscarentrenador, name="BuscarEntrenador"),
    path("nuevoslogros/", nuevoslogros, name="NuevosLogros"),
    path("buscarlogro/", buscarlogro, name="BuscarLogro")
]
