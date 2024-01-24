from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm, ProductoForm
from .models import Producto

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group

# Create your views here.
def home(request):
    return render(request, "index.html")

def productos(request):
    return render(request, "productos.html")

def contacto(request):
    data ={
        "form_contacto": ContactoForm,
        "mensaje": ""

    }

   
    if request.method == "POST":
        formulario= ContactoForm(data=request.POST)

        if formulario.is_valid():

            formulario.save()
            data["mensaje"] = "contacto creado"
        else:
            data["mensaje"] = "Error"
            data["form_contacto"] = formulario
    
    return render(request, "contacto.html", data)

    

def login(request):
    return render(request, "login.html")

def agregar_producto(request):
    data = {
        'form': ProductoForm
    }

    if request.method == "POST":
        formulario= ProductoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():

            formulario.save()
            data["mensaje"] = "Producto creado"
        else:
            data["mensaje"] = "Error"
            data["form"] = formulario

    return render(request, "mantenedor/producto/agregar.html", data)

def listar_producto(request):
    productos= Producto.objects.all()
    data = {
        'mis_productos' : productos
    }



    return render(request, "mantenedor/producto/listar.html", data)

def modificar_producto(request, id_buscado):

    productos= get_object_or_404(Producto, id=id_buscado)

    data = {
        'form' : ProductoForm(instance=productos)
    }

    if request.method == "POST":
        formulario= ProductoForm(data=request.POST, instance=productos, files=request.FILES)
    
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        else:
            data["mensaje"] = "hubo un Error"
            data["form"] = formulario

    return render(request, "mantenedor/producto/modificar.html", data)

def eliminar_producto(request, id_buscado):

    productos= get_object_or_404(Producto, id=id_buscado)

    productos.delete()

    return redirect(to= "listar_producto")


def login_usuario(request):
    print("Bienvenido:"+ request.user.username)
    return redirect(to="home")

def registro(request):
    data = {
        "mensaje": ""
    }

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password = request.POST.get("password")

        usu = User()
        usu.set_password(password) 
        usu.username = nombre
        usu.email = correo
        usu.first_name = nombre
        usu.last_name = apellido

        grupoVen = Group.objects.get(name="vendedor")

        try:
            usu.save()
            usu.groups.add(grupoVen)

            user = authenticate(username=usu.username, password=password)
            login(request, user)
            return redirect(to="home")

        except:
            data["mensaje"] = "Error Creado"

    return render(request, "registration/registro.html", data)