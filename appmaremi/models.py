from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Vendedor(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    telefono = models.IntegerField()
    correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.rut + " " + self.nombre

#json   
estados = [
    [0, "En Espera"],
    [1, "Aprobado"],
    [2, "Rechazado"]
]

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(null=True, upload_to='productos')
    precio = models.IntegerField(blank=False, null=False)
    fecha_compra = models.DateField(blank=False, null=False)
    mensaje = models.TextField()
    cantidad = models.IntegerField(null=True, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.IntegerField(choices=estados, default=0)

    def __str__(self):
        return f"{self.nombre}"

#json
list_tipo_contacto = [
    [0, "Sugerencia"],
    [1, "Reclamo"],
    [2, "Cambio"]
]

class Contacto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    mensaje = models.TextField()
    tipo_contacto = models.IntegerField(choices=list_tipo_contacto)

    def __str__(self):
        return self.nombre + " " + self.correo
