from django.urls import path
from . import views
from .views import AprendizFormView # Asegúrate que AprendizFormView esté importada

app_name = "aprendices"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("aprendices/", views.aprendices, name="lista_aprendices"),
    # URL para el formulario de agregar aprendiz
    path("aprendices/agregar/", AprendizFormView.as_view(), name="agregar_aprendiz"), # Ruta más específica y clara
    path("aprendices/aprendiz/<int:aprendiz_id>/", views.detalle_aprendiz, name="detalle_aprendiz"),
    
    # URLs de cursos (asumiendo que lista_cursos es la raíz para cursos dentro de aprendices)
    path("cursos/", views.lista_cursos, name="lista_cursos"),
    path("cursos/curso/<int:curso_id>/", views.detalle_curso, name="detalle_curso"),
]
