from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Curso, Semana, Sesion
from .serializers import CategoriaSerializer, CursoSerializer, SemanaSerializer, SesionSerializer

# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer

class SemanaViewSet(viewsets.ModelViewSet):
    queryset = Semana.objects.all()
    serializer_class = SemanaSerializer