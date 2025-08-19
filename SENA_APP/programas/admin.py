from django.contrib import admin
from .models import Programa

# Admin para Programa (mejorado)
@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "nombre",
        "nivel_formacion",
        "modalidad",
        "duracion_meses",
        "centro_formacion",
        "regional",
        "estado",
        "fecha_creacion",
    )
    list_filter = ("nivel_formacion", "modalidad", "estado", "regional", "centro_formacion")
    search_fields = (
        "codigo",
        "nombre",
        "descripcion",
        "centro_formacion",
        "regional",
    )
    list_per_page = 20
    ordering = ("nombre", "codigo")
    date_hierarchy = "fecha_creacion"

    fieldsets = (
        (
            "Información Básica",
            {"fields": (("codigo", "nombre"), ("nivel_formacion", "modalidad"), "estado")},
        ),
        (
            "Duración",
            {"fields": ("duracion_meses", "duracion_horas")},
        ),
        (
            "Contenido del Programa",
            {"fields": ("descripcion", "competencias", "perfil_egreso", "requisitos_ingreso")},
        ),
        (
            "Administración",
            {"fields": ("centro_formacion", "regional", "fecha_creacion")},
        ),
    )
