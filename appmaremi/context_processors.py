from .models import Categoria  # Ajusta la importación según la ubicación real de tu modelo

#para poder traerme todas las categorias 
def categorias_comunes(request):
    categorias = Categoria.objects.all()
    
    return {'categorias': categorias}