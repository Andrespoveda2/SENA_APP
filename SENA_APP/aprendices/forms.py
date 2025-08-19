from django import forms
from .models import Aprendiz

class AprendizForm(forms.Form):
    # Usamos CharField para documento_identidad para permitir validaciones de isdigit()
    # antes de convertir a int. Max_length según tu modelo.
    documento_identidad = forms.CharField(max_length=255, required=True, label="Documento de Identidad")
    nombre = forms.CharField(max_length=100, required=True, label="Nombre")
    apellido = forms.CharField(max_length=100, required=True, label="Apellido")
    # Teléfono es CharField para validación isdigit() y requerido=False como en el modelo (blank=True)
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono")
    # Correo no es requerido en el modelo, lo hacemos no requerido aquí
    correo = forms.EmailField(required=False, label="Correo Electrónico")
    # Campo para la fecha de nacimiento (minúscula para el form y para estandarizar el modelo)
    # Usamos DateInput con type='date' para un widget de calendario HTML5
    fecha_nacimiento = forms.DateField(required=True, label="Fecha de Nacimiento", widget=forms.DateInput(attrs={'type': 'date'}))
    # Ciudad y Programa son CharField y no requeridos
    ciudad = forms.CharField(max_length=100, required=False, label="Ciudad")
    programa = forms.CharField(max_length=100, required=False, label="Programa") # Añadido el campo 'programa'

    # Las validaciones 'clean' genéricas pueden ser útiles para lógica cruzada,
    # pero para campos individuales, 'required=True' ya maneja la obligatoriedad.
    # El método clean_documento_identidad ya lo estamos usando para int y isdigit.

    def clean_documento_identidad(self):
        documento = self.cleaned_data["documento_identidad"]
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        # Convertir a entero solo después de la validación exitosa
        return int(documento)

    def clean_telefono(self):
        telefono = self.cleaned_data.get("telefono")
        if telefono: # Solo validar si se proporcionó un teléfono
            if not telefono.isdigit():
                raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono

    # Método para guardar los datos del formulario en la base de datos
    def save(self):
        # Asegúrate de que los nombres de los campos aquí coincidan con los nombres del modelo (todos en minúscula ahora)
        Aprendiz.objects.create(
            documento_identidad=self.cleaned_data["documento_identidad"],
            nombre=self.cleaned_data["nombre"],
            apellido=self.cleaned_data["apellido"],
            telefono=self.cleaned_data.get("telefono"),
            correo=self.cleaned_data.get("correo"),
            fecha_nacimiento=self.cleaned_data["fecha_nacimiento"],
            ciudad=self.cleaned_data.get("ciudad"),
            programa=self.cleaned_data.get("programa"),
        )