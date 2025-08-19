from django.shortcuts import render, get_object_or_404, redirect # Añadido redirect para después del formulario
from .models import Aprendiz, Curso, AprendizCurso, InstructorCurso
from instructores.models import Instructor
from programas.models import Programa
from .forms import AprendizForm # Importamos nuestro formulario
from django.views import generic # Para usar FormView


def aprendices(request):
    lista_aprendices = Aprendiz.objects.all().order_by("apellido", "nombre")
    context = {
        "aprendices": lista_aprendices, # 'aprendices' es el nombre que usas en tu template
        "total_aprendices": lista_aprendices.count(),
    }
    return render(request, "lista_aprendices.html", context)


def inicio(request):
    # Estadísticas generales
    total_aprendices = Aprendiz.objects.count()
    total_instructores = Instructor.objects.count()
    total_programas = Programa.objects.count()
    total_cursos = Curso.objects.count()
    cursos_activos = Curso.objects.filter(estado__in=["INI", "EJE"]).count()

    context = {
        "total_aprendices": total_aprendices,
        "total_cursos": total_cursos,
        "cursos_activos": cursos_activos,
        "total_instructores": total_instructores,
        "total_programas": total_programas,
    }
    return render(request, "inicio.html", context)


def lista_cursos(request):
    cursos = Curso.objects.all().order_by("-fecha_inicio")
    context = {
        "lista_cursos": cursos,
        "total_cursos": cursos.count(),
        "titulo": "Lista de Cursos",
    }
    return render(request, "lista_cursos.html", context)


def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    aprendices_curso = AprendizCurso.objects.filter(curso=curso)
    instructores_curso = InstructorCurso.objects.filter(curso=curso)
    context = {
        "curso": curso,
        "aprendices_curso": aprendices_curso,
        "instructores_curso": instructores_curso,
    }
    return render(request, "detalle_curso.html", context)


def detalle_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)
    cursos_inscritos = AprendizCurso.objects.filter(aprendiz=aprendiz)
    context = {
        "aprendiz": aprendiz,
        "cursos_inscritos": cursos_inscritos,
    }
    return render(request, "detalle_aprendiz.html", context)


# Vista para el formulario de agregar aprendiz (basada en la de tu amigo)
class AprendizFormView(generic.FormView):
    template_name = "agregar_aprendiz.html" # Ruta sin subcarpeta 'aprendices/'
    form_class = AprendizForm
    # success_url = "../aprendices/" # Esta ruta relativa es frágil.
    # Mejor usar una URL absoluta o un reverse_lazy para mayor robustez
    success_url = '/aprendices/'

    def form_valid(self, form):
        # Este método es llamado cuando el formulario es válido.
        # Aquí es donde se guarda el nuevo aprendiz en la base de datos.
        form.save() # Llama al método save() que definimos en AprendizForm
        return super().form_valid(form) # Redirige a success_url

