from django import forms
from .models import Instructor

class InstructorForm(forms.ModelForm): # Usamos ModelForm para mayor facilidad
    class Meta:
        model = Instructor
        fields = [
            'documento_identidad',
            'tipo_documento',
            'nombre',
            'apellido',
            'telefono',
            'correo',
            'fecha_nacimiento',
            'ciudad',
            'direccion',
            'nivel_educativo',
            'especialidad',
            'anios_experiencia',
            'activo',
            'fecha_vinculacion',
        ]
        # Widgets para campos de fecha para usar selectores HTML5
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_vinculacion': forms.DateInput(attrs={'type': 'date'}),
        }
        # Etiquetas personalizadas si deseas algo diferente a verbose_name
        labels = {
            'documento_identidad': 'Documento de Identidad',
            'tipo_documento': 'Tipo de Documento',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'nivel_educativo': 'Nivel Educativo',
            'anios_experiencia': 'Años de Experiencia',
            'fecha_vinculacion': 'Fecha de Vinculación',
        }

    # Validaciones personalizadas (ejemplo)
    def clean_documento_identidad(self):
        documento = self.cleaned_data['documento_identidad']
        # Si tu campo en el modelo es IntegerField, Django ya valida que sea un número.
        # Pero si quieres validaciones adicionales (ej. longitud específica) las puedes poner aquí.
        # Ejemplo: if len(str(documento)) != 10: raise forms.ValidationError("El documento debe tener 10 dígitos.")
        return documento

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not str(telefono).isdigit(): # Convertir a string para isdigit()
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono
    