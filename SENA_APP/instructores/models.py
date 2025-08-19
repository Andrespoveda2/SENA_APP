from django.db import models


class Instructor(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ("CC", "Cédula de Ciudadanía"),
        ("CE", "Cédula de Extranjería"),
        ("TI", "Tarjeta de Identidad"),
        ("PAS", "Pasaporte"),
    ]
    NIVEL_EDUCATIVO_CHOICES = [
        ("TEC", "Técnico"),
        ("TGL", "Tecnólogo"),
        ("PRE", "Pregrado"),
        ("ESP", "Especialización"),
        ("MAE", "Maestría"),
        ("DOC", "Doctorado"),
    ]

    documento_identidad = models.IntegerField(unique=True)
    tipo_documento = models.CharField(
        max_length=3, choices=TIPO_DOCUMENTO_CHOICES, default="CC"
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField(null=True, blank=True) # Permitir nulos y vacíos
    correo = models.EmailField(max_length=100, null=True, blank=True) # Permitir nulos y vacíos
    fecha_nacimiento = models.DateField() # Campo requerido
    ciudad = models.CharField(max_length=100, null=True, blank=True) # Permitir nulos y vacíos
    direccion = models.TextField(null=True, blank=True) # Permitir nulos y vacíos
    nivel_educativo = models.CharField(
        max_length=3, choices=NIVEL_EDUCATIVO_CHOICES, default="MAE", null=True, blank=True # Permite no ser seleccionado
    )
    especialidad = models.CharField(max_length=100) # Campo requerido
    anios_experiencia = models.PositiveIntegerField() # Campo requerido (corregido de 'anos_experiencia')
    activo = models.BooleanField(default=True) # Campo requerido
    fecha_vinculacion = models.DateField() # Campo requerido

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructores"
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.documento_identidad}"

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

