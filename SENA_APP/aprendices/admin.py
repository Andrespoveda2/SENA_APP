# aprendices/admin.py

from django.contrib import admin
from .models import Aprendiz

@admin.register(Aprendiz)
class AprendizAdmin(admin.ModelAdmin):
    list_display = ('documento_identidad', 'nombre', 'apellido', 'programa')
    search_fields = ('nombre', 'apellido', 'programa')
    list_filter = ('ciudad', 'programa')
    ordering = ('apellido',)
    list_per_page = 10
