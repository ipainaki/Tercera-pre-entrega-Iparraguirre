from django import forms
 
class JugadorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    numero = forms.IntegerField()

class BuscarJugadorForm(forms.Form):
    apellido = forms.CharField()




class EntrenadorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()

class BuscarEntrenadorForm(forms.Form):
    apellido = forms.CharField()




class LogroFormulario(forms.Form):
    nombre = forms.CharField()
    ano = forms.IntegerField()

class BuscarLogroForm(forms.Form):
    nombre = forms.CharField()