from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista_aprendices/', views.aprendices, name='lista_aprendices'),
]


