from django.shortcuts import render
from App.models import Jugador, Entrenador, Logro
from App.forms import JugadorFormulario, BuscarJugadorForm, EntrenadorFormulario, BuscarEntrenadorForm, LogroFormulario, BuscarLogroForm
def inicio(request):
	return render(request, "App/inicio.html")
def jugadores(request):
      lista_jugadores = Jugador.objects.all()
      return render(request, "App/jugadores.html", {"jugadores": lista_jugadores})
def entrenadores(request):
      lista_entrenadores = Entrenador.objects.all()
      return render(request, "App/entrenadores.html", {"entrenadores": lista_entrenadores})
def logros(request):
      lista_logros = Logro.objects.all()
      return render(request, "App/logros.html", {"logros": lista_logros})

def nuevosjugadores(request):
 
      if request.method == "POST":
 
            miFormulario = JugadorFormulario(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  jugador = Jugador (nombre=informacion["nombre"], apellido=informacion["apellido"], numero=informacion["numero"])
                  jugador.save()
                  return render(request, "App/inicio.html")
      else:
            miFormulario = JugadorFormulario()
 
      return render(request, "App/nuevosjugadores.html", {"miFormulario": miFormulario})
def buscarjugador(request):
      if request.method == "POST":
 
            miFormulario = BuscarJugadorForm(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  jugadores = Jugador.objects.filter(apellido__icontains=informacion["apellido"])
             
                  return render(request, "App/listajugadores.html", {"jugadores": jugadores})
      else:
            miFormulario = BuscarJugadorForm()
 
      return render(request, "App/filtrojugadores.html", {"miFormulario": miFormulario})


def nuevosentrenadores(request):
 
      if request.method == "POST":
 
            miFormulario = EntrenadorFormulario(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  entrenador = Entrenador (nombre=informacion["nombre"], apellido=informacion["apellido"], edad=informacion["edad"])
                  entrenador.save()
                  return render(request, "App/inicio.html")
      else:
            miFormulario = EntrenadorFormulario()
 
      return render(request, "App/nuevosentrenadores.html", {"miFormulario": miFormulario})
def buscarentrenador(request):
      if request.method == "POST":
 
            miFormulario = BuscarEntrenadorForm(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  entrenadores= Entrenador.objects.filter(apellido__icontains=informacion["apellido"])
             
                  return render(request, "App/listaentrenadores.html", {"entrenadores": entrenadores})
      else:
            miFormulario = BuscarEntrenadorForm()
 
      return render(request, "App/filtroentrenadores.html", {"miFormulario": miFormulario})


def nuevoslogros(request):
 
      if request.method == "POST":
 
            miFormulario = LogroFormulario(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  logro = Logro (nombre=informacion["nombre"], ano=informacion["ano"])
                  logro.save()
                  return render(request, "App/inicio.html")
      else:
            miFormulario = LogroFormulario()
 
      return render(request, "App/nuevoslogros.html", {"miFormulario": miFormulario})
def buscarlogro(request):
      if request.method == "POST":
 
            miFormulario = BuscarLogroForm(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  logros = Logro.objects.filter(nombre__icontains=informacion["nombre"])
             
                  return render(request, "App/listalogros.html", {"logros": logros})
      else:
            miFormulario = BuscarLogroForm()
 
      return render(request, "App/filtrologros.html", {"miFormulario": miFormulario})

# Create your views here.
