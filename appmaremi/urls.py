
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('productos', productos, name="productos"),
    path('contacto', contacto, name="contacto"),
    path('login', login, name="login"),
    path('mantenedor/agregar_producto/', agregar_producto, name="agregar_producto"),
    path('mantenedor/listar_producto/', listar_producto, name="listar_producto"),
    path('mantenedor/modificar_producto/<id_buscado>/', modificar_producto, name="modificar_producto"),
    path('mantenedor/eliminar_producto/<id_buscado>/',  eliminar_producto, name="eliminar_producto"),
    path('login_usuario/', login_usuario, name='login_usuario'),
    path('registro/', registro, name='registro'),
  

]
