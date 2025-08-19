from django.contrib import admin
from .models import Instructor
# Si necesitas InstructorCurso en este admin.py (por ejemplo, para inlines en otros modelos
# o para registrarlo directamente aquí), impórtalo desde la app correcta:
# from aprendices.models import InstructorCurso


# Admin para Instructor (mejorado)
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        "documento_identidad",
        "tipo_documento", # Añadido para mostrar el tipo
        "nombre_completo",
        "correo",
        "telefono",
        "ciudad",
        "especialidad",
        "activo",
    )
    list_filter = ("activo", "nivel_educativo", "especialidad", "ciudad", "tipo_documento") # Añadido tipo_documento al filtro
    search_fields = (
        "documento_identidad",
        "nombre",
        "apellido",
        "correo",
        "especialidad",
    )
    list_per_page = 20
    ordering = ("apellido", "nombre")
    date_hierarchy = "fecha_vinculacion" # Para navegación por fechas en el admin

    fieldsets = (
        (
            "Información Personal",
            {
                "fields": (
                    ("tipo_documento", "documento_identidad"), # Campos en la misma línea
                    ("nombre", "apellido"),
                    "fecha_nacimiento",
                    "activo",
                )
            },
        ),
        (
            "Contacto y Ubicación",
            {"fields": ("telefono", "correo", "ciudad", "direccion")},
        ),
        (
            "Información Profesional",
            {"fields": ("nivel_educativo", "especialidad", "anios_experiencia", "fecha_vinculacion")}, # Corregido: 'anios_experiencia'
        ),
    )

    def nombre_completo(self, obj):
        # Asume que el modelo Instructor tiene un método nombre_completo
        # Si no, usa: return f"{obj.nombre} {obj.apellido}"
        return f"{obj.nombre} {obj.apellido}"

    nombre_completo.short_description = "Nombre Completo"