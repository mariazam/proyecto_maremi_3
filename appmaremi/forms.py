from django import forms 
from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):
    class Meta:
        model= Contacto
        fields = "__all__"

class ProductoForm(forms.ModelForm):
    class Meta:
        model= Producto
        fields = "__all__"
        #este arregla el formato de la fecha al ingresar un producto en el formulario
        widgets = {
            "fecha_compra": forms.DateInput(attrs={'type':'date'}, format=('%Y-%m-%d'))
        }