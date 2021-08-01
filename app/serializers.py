from django.db.models import fields
from rest_framework import serializers
from .models import Beneficio, Categoria, Curso, CursoBeneficio, Horario, HorarioCurso, Semana, Sesion, SesionCurso


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'categoria']

class CursoSerializer(serializers.ModelSerializer):

    id_categoria = CategoriaSerializer(many=False)

    class Meta:
        model = Curso
        fields = ['id', 'curso', 'duracion', 'precio', 'id_categoria', 'url']


class SesionSerializer(serializers.ModelSerializer):

    #id_curso = CursoSerializer(many=False)

    class Meta:
        model = Sesion
        fields = ['id', 'sesion']


class SesionCursoSerializer(serializers.ModelSerializer):
    
    id_sesion = SesionSerializer(many=False)
    id_curso = CursoSerializer(many=False)

    class Meta:
        model = SesionCurso
        fields = ['id', 'id_curso', 'id_sesion']

class SemanaSerializer(serializers.ModelSerializer):
    
    id_sesioncurso = SesionCursoSerializer(many=False)

    class Meta:
        model = Semana
        fields = ['id', 'id_sesioncurso', 'semana', 'descripcion']



class HorarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horario
        fields = ['id', 'frecuencia', 'horaInicio', 'horaFin']


class HorarioCursoSerializer(serializers.ModelSerializer):

    id_horario = HorarioSerializer(many=False)
    id_curso = CursoSerializer(many=False)


    class Meta:
        model = HorarioCurso
        fields = ['id', 'id_curso', 'id_horario']

class BeneficioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beneficio
        fields = ['id', 'beneficio']

class CursoBeneficioSerialzer(serializers.ModelSerializer):

    curso = CursoSerializer(many=False)
    beneficio = BeneficioSerializer(many=False)

    class Meta:
        model = CursoBeneficio
        fields = ['id', 'curso', 'beneficio']

