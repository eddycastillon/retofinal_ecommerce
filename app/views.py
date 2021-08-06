from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Beneficio, Categoria, Curso, CursoDetalle, Descuento, Interesado, Semana, Sesion, Horario, HorarioCurso, SesionCurso
from .serializers import BeneficioSerializer, CategoriaSerializer, CursoDetalleSerializer, CursoSerializer, DescuentoSerializer, InteresadoSerializer, SemanaSerializer, SesionSerializer, \
    HorarioSerializer, HorarioCursoSerializer, SesionCursoSerializer,\
        DescuentoSerializer, InteresadoSerializer, CursoDetalleSerializer

# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class CursoDetalleViewSet(viewsets.ModelViewSet):
    queryset = CursoDetalle.objects.all()
    serializer_class = CursoDetalleSerializer

    def retrieve(self, request, pk=None):
        curso_id  = self.kwargs['pk']
        queryset = CursoDetalle.objects.filter(curso_id = curso_id).first()
        serializer_class = CursoDetalleSerializer(queryset)
        return Response(serializer_class.data)
     

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