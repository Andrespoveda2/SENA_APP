from django.urls import path
from . import views
from .views import ProgramaFormView # Importación correcta

app_name = "programas"

urlpatterns = [
    path("programas/", views.programas, name="lista_programas"),
    # URL para el formulario de agregar programa
    path("programas/agregar/", ProgramaFormView.as_view(), name="agregar_programa"),
    path(
        "programas/programa/<int:programa_id>/",
        views.detalle_programa,
        name="detalle_programa",
    ),
]