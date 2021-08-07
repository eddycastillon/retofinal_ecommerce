from rest_framework.fields import ReadOnlyField
import shortuuid
from django.db.models import fields
from rest_framework import serializers
from .models import Beneficio, Categoria, Curso, Descuento, Horario, HorarioCurso, Semana, Sesion, SesionCurso, \
     Interesado, Descuento, CursoDetalle



class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'categoria']

class CursoSerializer(serializers.ModelSerializer):

    id_categoria = CategoriaSerializer(many=False)

    class Meta:
        model = Curso
        fields = ['id', 'curso', 'duracion', 'precio', 'id_categoria', 'url']

class CursoDetalleSerializer(serializers.ModelSerializer):
    curso_id = CursoSerializer(many=False)

    class Meta:
        model = CursoDetalle
        fields = '__all__'

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

class InteresadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Interesado
        fields = ['id', 'nombres', 'apellido_paterno', 'apellido_materno', 'celular', 'email']

    

class DescuentoSerializer(serializers.ModelSerializer):
    
    interesado_id = InteresadoSerializer(many=False)

    class Meta:
        model = Descuento
        fields = ['id', 'interesado_id', 'status', 'codigo']
        #read_only_fields = ['interesado_id']

    def create(self, data):
        interesado_id = Interesado.objects.create(**data['interesado_id'])
        status = data['status']
        codigo = shortuuid.ShortUUID().random(length=8)
        return Descuento.objects.create(interesado_id = interesado_id, status = status, codigo = codigo)
