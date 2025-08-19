from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy # Para success_url robusto
from django.contrib import messages
from django.views.generic import FormView

from .models import Programa
from .forms import ProgramaForm # Importamos el formulario que creamos

# Vista para mostrar la lista de programas
def programas(request):
    lista_programas = Programa.objects.all().order_by("nombre") # Ordenamos por nombre
    context = {
        "lista_programas": lista_programas,
        "total_programas": lista_programas.count(),
    }
    return render(request, "lista_programas.html", context)


# Vista para mostrar los detalles de un programa
def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id)
    # Asume que tienes un 'related_name' en tu modelo Curso apuntando a Programa,
    # o que Django crea uno por defecto como 'curso_set'.
    cursos = programa.curso_set.all().order_by("-fecha_inicio")
    
    context = {
        "programa": programa,
        "cursos": cursos,
    }
    return render(request, "detalle_programa.html", context)


# Vista basada en clases para el formulario de agregar programa
class ProgramaFormView(FormView):
    template_name = "agregar_programa.html"
    form_class = ProgramaForm
    # Usamos reverse_lazy para que la URL se resuelva después de que Django cargue todas las URLs
    success_url = reverse_lazy('programas:lista_programas')

    def form_valid(self, form):
        # ModelForm.save() crea y guarda la instancia del modelo automáticamente
        programa = form.save()
        messages.success(
            self.request,
            f"El programa '{programa.nombre}' ha sido registrado exitosamente."
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija los errores en el formulario.")
        # Opcional: imprimir errores para depuración en la consola
        # print("Errores del formulario:", form.errors)
        return super().form_invalid(form)
