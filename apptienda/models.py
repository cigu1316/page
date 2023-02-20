from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now_add=True)   

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tienda')    
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now_add=True)
    descripcion = models.TextField(max_length=200, blank=True, null=True)
    codigo = models.IntegerField(max_length=10)
    
    
    def __str__(self):
        return self.nombre