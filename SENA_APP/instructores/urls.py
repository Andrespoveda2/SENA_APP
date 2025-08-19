from django.urls import path
from . import views
from .views import InstructorFormView # Importación correcta

app_name = "instructores"

urlpatterns = [
    path("instructores/", views.instructores, name="lista_instructores"),
    # URL para el formulario de agregar instructor
    path("instructores/agregar/", InstructorFormView.as_view(), name="agregar_instructor"),
    path(
        "instructores/instructor/<int:instructor_id>/",
        views.detalle_instructor,
        name="detalle_instructor",
    ),
]