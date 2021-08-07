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
        serializer_class = CursoDetalleSerializer(queryset, many=True)
        return Response(serializer_class.data)
     

class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer

class SesionCursoViewSet(viewsets.ModelViewSet):
    queryset = SesionCurso.objects.all()
    serializer_class = SesionCursoSerializer

    def retrieve(self, request, pk=None):
        id_curso  = self.kwargs['pk']
        queryset = SesionCurso.objects.filter(id_curso = id_curso).all()
        serializer_class = SesionCursoSerializer(queryset, many=True)
        return Response(serializer_class.data)

class SemanaViewSet(viewsets.ModelViewSet):
    queryset = Semana.objects.all()
    serializer_class = SemanaSerializer

    def retrieve(self, request, pk=None):
        id_sesioncurso  = self.kwargs['pk']
        queryset = Semana.objects.filter(id_sesioncurso = id_sesioncurso).all()
        serializer_class = SemanaSerializer(queryset, many=True)
        return Response(serializer_class.data)

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class HorarioCursoViewSet(viewsets.ModelViewSet):
    queryset = HorarioCurso.objects.all()
    serializer_class = HorarioCursoSerializer

    def retrieve(self, request, pk=None):
        id_curso  = self.kwargs['pk']
        queryset = HorarioCurso.objects.filter(id_curso = id_curso).all()
        serializer_class = HorarioCursoSerializer(queryset, many=True)
        return Response(serializer_class.data)

class BeneficioViewSet(viewsets.ModelViewSet):
    queryset = Beneficio.objects.all()
    serializer_class = BeneficioSerializer

class InteresadoViewSet(viewsets.ModelViewSet):
    queryset = Interesado.objects.all()
    serializer_class = InteresadoSerializer        
 
class DescuentoViewSet(viewsets.ModelViewSet):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer 