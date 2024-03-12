from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm, ProductoForm
from .models import Categoria, Producto
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):

    productos = Producto.objects.all()
    return render(request, "index.html",{'productos': productos})

# def carrusel(request):
#     productos = Producto.objects.all()
#     return render(request, "index.html",{'productos': productos})

def productos(request):
    return render(request, "productos.html")

#vista contanto save() si la persona envia algo entra al post y lo guarda
#si no envia un mensaje de error y lo vuelve a dirijir a la vista del contacto
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

    
#vista login
def login(request):
    return render(request, "login.html")

#login_required=restrinje que alguien que no tenga permiso entre a la pg y lo dirije al login
#permission_required = restrinje que alguien que no tenga permiso entre a la pg y lo dirije al login que solo pueda el admin
@login_required(login_url="login")
@permission_required(['appmaremi.add_producto'], login_url="login")
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

#login_required=restrinje que alguien que no tenga permiso entre a la pg y lo dirije al login
#permission_required = restrinje que alguien que no tenga permiso entre a la pg y lo dirije al login que solo pueda el admin
@login_required(login_url="login")
@permission_required(['appmaremi.add_producto'], login_url="login")
def listar_producto(request):
    productos= Producto.objects.all()

    data = {
        'mis_productos' : productos
    }

    return render(request, "mantenedor/producto/listar.html", data)

#listar producto el vendedor 
def listarProducto_vendedor(request):
    productos= Producto.objects.all()

    data = {
        'mis_productos' : productos
    }

    return render(request, "mantenedor/vendedor/listarProducto_vendedor.html", data)

#login_required=restrinje que alguien que no tenga permiso entre a la pg y lo dirije al login
#permission_required = restrinje que alguien que no tenga permiso entre a la pg y lo dirije al login que solo pueda el admin
@login_required(login_url="login")
@permission_required(['appmaremi.add_producto'], login_url="login")
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

#este  se usa en el listar
#get_object_or_404 Es una función llama al modelo dado y obtiene el objeto de eso.

def eliminar_producto(request, id_buscado):

    productos= get_object_or_404(Producto, id=id_buscado)

    productos.delete()

    return redirect(to= "listar_producto")

#cuando se loguean muestra el mensaje del nombre de quien se a logiado y lo dirije al home
def login_usuario(request):
    print("Bienvenido:"+ request.user.username)
    return redirect(to="home")

#metodo de registrar usuarios  solo el admin 
@login_required(login_url="login")
@permission_required(['appmaremi.add_producto'], login_url="login")
def registro(request):

    data = {
        "mensaje": ""
    }

    if request.method == "POST":

        nombre = request.POST.get("nombre")  #request.POST.get("nombre") para obtener ese dato
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


#vista del administrador
def administrador(request):

    return render(request, "administrador.html")

#vista del administrador
def vendedor(request):

    return render(request, "vendedor.html")


#Metodo para poder distingir los usuarios logiados
#este metodo ayuda a distingir si el usuario es vendedor o admin a
#pero no funciona por hacer 

def tu_vista(request):
    # ... tu lógica para obtener el usuario
        
    es_administrador = request.user.groups.filter(name='administrador').exists()

    return render(request, 'administrador.html', {'es_administrador': es_administrador})


#es para poder mandar todos los productos a productos y listarlos todos
#producto
def listar_productos2(request):
    productos = Producto.objects.all()
    return render(request, "productos.html",{'productos': productos})

#vista del administrador
def detalleProducto(request, producto_id):

    producto = get_object_or_404(Producto, pk=producto_id)
    
    return render(request, 'detalleProducto.html', {'producto': producto})

#listar por cada categoria 
#use Producto.objects.filter(categoria = categoria_id, estado=1)
#para que dar una codicion de que el id categoria sea igual al id categoria que me pasa y sea estado 1
#aprobado para pasarselo al listar por categoria ya filtrado 
def listar_categoria(request, categoria_id):
    
    productos = Producto.objects.filter(categoria = categoria_id, estado=1)
    data = {'productos': productos}

    return render(request, "listar_categoria.html", data)


#no va 
def buscar_producto(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        resultados = Producto.objects.filter(nombre__icontains=query)
        return render(request, 'buscar_producto.html', {'resultados': resultados})
    else:
        return render(request, 'buscar_producto.html')
    
#vista del administrador
def videos(request):

    return render(request, "video.html")

def buscar_productos(request):
    query = request.GET.get('q', '')  # Obtiene la consulta de búsqueda desde la URL
    resultados = Producto.objects.filter(nombre__icontains=query)  # Filtra los productos según la consulta

    return render(request, 'buscar_productos.html', {'resultados': resultados, 'query': query})