from django.shortcuts import render
from App.models import Blog, Avatar
from App.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
      return render(request, "App/inicio.html")


class BlogList(LoginRequiredMixin, ListView):
      model = Blog
      template_name = "App/blogs_list.html"
class BlogDetalle(DetailView):
      model = Blog
      template_name = "App/blogs_detalle.html"
class BlogCreacion(LoginRequiredMixin, CreateView):
      model = Blog
      template_name = "App/blogs_create.html"
      success_url = reverse_lazy("List")
      fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']
class BlogUpdate(UpdateView):
      model = Blog
      template_name = "App/blogs_edit.html"
      success_url = reverse_lazy("List")
      fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']
class BlogDelete(DeleteView):
      model = Blog
      template_name = "App/blogs_delete.html"
      success_url = reverse_lazy("List")

def login_request(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

                  if user is not None:
                        login(request, user)
                       
                        return render(request,"App/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )

            else:
                        
                        return render(request,"App/inicio.html" ,  {"mensaje":"Error, datos incorrectos"})

      form = AuthenticationForm()

      return render(request,"App/login.html", {'form':form} )

def register(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"App/inicio.html" ,  {"mensaje":"Usuario Creado"})
            else:
                  return render(request,"App/inicio.html" ,  {"mensaje":"no cumple requisitos"})
      else:
            form = UserRegisterForm()            

      return render(request,"App/register.html" ,  {"form":form})

@login_required
def useredit(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.username = informacion['username']

            usuario.save()

            return render(request, "App/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "App/useredit.html", {"form": miFormulario, "usuario": usuario})





# Create your views here.
