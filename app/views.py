from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Curso
from .serializers import CategoriaSerializer, CursoSerializer

# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer