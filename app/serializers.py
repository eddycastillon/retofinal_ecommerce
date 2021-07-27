from django.db.models import fields
from rest_framework import serializers
from .models import Categoria, Curso


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'categoria']

class CursoSerializer(serializers.ModelSerializer):

    id_categoria = CategoriaSerializer(many=False)

    class Meta:
        model = Curso
        fields = ['id', 'curso', 'duracion', 'precio', 'id_categoria']