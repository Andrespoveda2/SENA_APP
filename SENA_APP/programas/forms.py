from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = [
            'codigo',
            'nombre',
            'nivel_formacion',
            'modalidad',
            'duracion_meses',
            'duracion_horas',
            'descripcion',
            'competencias',
            'perfil_egreso',
            'requisitos_ingreso',
            'centro_formacion',
            'regional',
            'estado',
            'fecha_creacion',
            # 'fecha_registro' se excluye porque tiene auto_now_add=True
        ]
        # Widgets para campos de fecha y TextAreas
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'competencias': forms.Textarea(attrs={'rows': 4}),
            'perfil_egreso': forms.Textarea(attrs={'rows': 4}),
            'requisitos_ingreso': forms.Textarea(attrs={'rows': 4}),
            'fecha_creacion': forms.DateInput(attrs={'type': 'date'}),
        }
        # Etiquetas personalizadas para mayor claridad
        labels = {
            'codigo': 'Código del Programa',
            'nombre': 'Nombre del Programa',
            'nivel_formacion': 'Nivel de Formación',
            'duracion_meses': 'Duración (Meses)',
            'duracion_horas': 'Duración (Horas)',
            'descripcion': 'Descripción',
            'competencias': 'Competencias a Desarrollar',
            'perfil_egreso': 'Perfil de Egreso',
            'requisitos_ingreso': 'Requisitos de Ingreso',
            'centro_formacion': 'Centro de Formación',
            'fecha_creacion': 'Fecha de Creación',
        }

    # Puedes añadir validaciones personalizadas aquí
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if Programa.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError("Ya existe un programa con este código.")
        return codigo