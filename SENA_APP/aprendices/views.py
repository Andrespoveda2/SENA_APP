from django.shortcuts import render
from .models import Aprendiz

def inicio(request):
    return render(request, 'inicio.html')

def aprendices(request):
    lista_aprendices = Aprendiz.objects.all()
    return render(request, 'lista_aprendices.html', {'aprendices': lista_aprendices})

