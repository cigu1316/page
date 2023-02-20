from django.contrib import admin
from apptienda.models import Categoria, Producto


@admin.register(Categoria)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_display_links = ('id','nombre')
    search_fields = ('nombre',)

@admin.register(Producto)
class productoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','categoria','precio')
    list_display_links = ('id','nombre')
    search_fields = ('nombre',)

