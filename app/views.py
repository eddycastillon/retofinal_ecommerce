from django.shortcuts import render
from rest_framework import viewsets
from .models import Beneficio, Categoria, Curso, Descuento, Interesado, Semana, Sesion, Horario, HorarioCurso, SesionCurso
from .serializers import BeneficioSerializer, CategoriaSerializer, CursoSerializer, DescuentoSerializer, InteresadoSerializer, SemanaSerializer, SesionSerializer, \
    HorarioSerializer, HorarioCursoSerializer, SesionCursoSerializer,\
        DescuentoSerializer, InteresadoSerializer

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

class SesionCursoViewSet(viewsets.ModelViewSet):
    queryset = SesionCurso.objects.all()
    serializer_class = SesionCursoSerializer

class SemanaViewSet(viewsets.ModelViewSet):
    queryset = Semana.objects.all()
    serializer_class = SemanaSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class HorarioCursoViewSet(viewsets.ModelViewSet):
    queryset = HorarioCurso.objects.all()
    serializer_class = HorarioCursoSerializer

class BeneficioViewSet(viewsets.ModelViewSet):
    queryset = Beneficio.objects.all()
    serializer_class = BeneficioSerializer

class InteresadoViewSet(viewsets.ModelViewSet):
    queryset = Interesado.objects.all()
    serializer_class = InteresadoSerializer

class DescuentoViewSet(viewsets.ModelViewSet):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer