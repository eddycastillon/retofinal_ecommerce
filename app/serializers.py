from django.db.models import fields
from rest_framework import serializers
from .models import Categoria, Curso, Semana, Sesion


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'categoria']

class CursoSerializer(serializers.ModelSerializer):

    id_categoria = CategoriaSerializer(many=False)

    class Meta:
        model = Curso
        fields = ['id', 'curso', 'duracion', 'precio', 'id_categoria']


class SesionSerializer(serializers.ModelSerializer):

    #id_curso = CursoSerializer(many=False)

    class Meta:
        model = Sesion
        fields = ['id', 'sesion', 'id_curso']

class SemanaSerializer(serializers.ModelSerializer):
    
    #id_sesion = SesionSerializer(many=False)

    class Meta:
        model = Semana
        fields = ['id', 'id_sesion', 'semana', 'descripcion']

