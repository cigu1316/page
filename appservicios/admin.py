from django.contrib import admin
from .models import Servicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo','created','updated')
    list_filter = ('titulo','created','updated')
    search_fields = ('titulo','contenido')
    date_hierarchy = 'created'
    ordering = ('titulo','created','updated')
    readonly_fields = ('created','updated')
    
