from django.urls import path
from .views import inicio, BlogList, BlogDetalle, BlogCreacion, BlogUpdate, BlogDelete, login_request, register, useredit
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name="Inicio"),
    path("blogs/list/", BlogList.as_view(), name="List"),
    path("blogs/detalle/<int:pk>/", BlogDetalle.as_view(), name="Detail"),
    path("blogs/nuevo/", BlogCreacion.as_view(), name="New"),
    path("blogs/editar/<int:pk>/", BlogUpdate.as_view(), name="Edit"),
    path("blogs/eliminar/<int:pk>/", BlogDelete.as_view(), name="Delete"),
    path("login/", login_request, name="Login"),
    path('register/', register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='App/logout.html'), name='Logout'),
    path('useredit/', useredit, name="Useredit")

]
