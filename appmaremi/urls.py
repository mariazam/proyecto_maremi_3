
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('productos/', listar_productos2, name='productos'),
    path('contacto', contacto, name="contacto"),
    path('login', login, name="login"),
    path('mantenedor/agregar_producto/', agregar_producto, name="agregar_producto"),
    path('mantenedor/listar_producto/', listar_producto, name="listar_producto"),
    path('mantenedor/modificar_producto/<id_buscado>/', modificar_producto, name="modificar_producto"),
    path('mantenedor/eliminar_producto/<id_buscado>/',  eliminar_producto, name="eliminar_producto"),
    path('login_usuario/', login_usuario, name='login_usuario'),
    path('registro/', registro, name='registro'),
    path('administrador/', administrador, name='vista_administrador'),
    path('vendedor/', vendedor, name='vista_vendedor'),
    path('detalleProducto/<int:producto_id>/', detalleProducto, name='detalleProducto'),
    path('listar_categoria/<int:categoria_id>/', listar_categoria, name='listar_categoria'),  
    path('mantenedor/listarProducto_vendedor/', listarProducto_vendedor, name="listarProducto_vendedor"),
    path('videos', videos, name="videos"),
    path('buscar/', buscar_productos, name='buscar_productos'),


]
