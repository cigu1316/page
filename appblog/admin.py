from django.contrib import admin
from appblog.models import Categorias , Post


@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
