from django.shortcuts import render
from . models import Estudiante

def tabla(request):
    estudiante = Estudiante.objects.all()
    return render(request, 'index.html',{'estudiantes': estudiante})