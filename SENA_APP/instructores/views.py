from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy # Mejor para success_url
from django.contrib import messages
from django.views.generic import FormView

from .models import Instructor
from .forms import InstructorForm # Importamos nuestro ModelForm

# Vista para mostrar la lista de instructores
def instructores(request):
    lista_instructores = Instructor.objects.all().order_by("apellido", "nombre")
    context = {
        "lista_instructores": lista_instructores,
        "total_instructores": lista_instructores.count(),
    }
    return render(request, "lista_instructores.html", context)


# Vista para mostrar los detalles de un instructor
def detalle_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    # Estos related_names deben estar definidos en tus modelos (Curso)
    # Si tus modelos de Curso, InstructorCurso están en 'aprendices/models.py',
    # asegúrate de que Instructor tenga 'related_name' adecuados o impórtalos aquí.
    # Por ejemplo: from aprendices.models import Curso, InstructorCurso
    cursos_coordinados = instructor.cursos_coordinados.all() if hasattr(instructor, 'cursos_coordinados') else []
    cursos_impartidos = instructor.cursos_impartidos.all() if hasattr(instructor, 'cursos_impartidos') else []
    
    context = {
        "instructor": instructor,
        "cursos_coordinados": cursos_coordinados,
        "cursos_impartidos": cursos_impartidos,
    }
    return render(request, "detalle_instructor.html", context)


# Vista basada en clases para el formulario de agregar instructor
class InstructorFormView(FormView):
    template_name = "agregar_instructor.html"
    form_class = InstructorForm
    # Usamos reverse_lazy para asegurarnos de que la URL se resuelva después de que Django cargue todas las URLs
    success_url = reverse_lazy('instructores:lista_instructores') 

    def form_valid(self, form):
        # ModelForm.save() crea y guarda la instancia del modelo automáticamente
        instructor = form.save() 
        messages.success(
            self.request,
            f"El instructor '{instructor.nombre} {instructor.apellido}' ha sido registrado exitosamente."
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija los errores en el formulario.")
        # Opcional: imprimir errores para depuración en la consola
        # print("Errores del formulario:", form.errors)
        return super().form_invalid(form)
