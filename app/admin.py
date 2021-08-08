from django.contrib import admin
from .models import Beneficio, Categoria, Curso, CursoDetalle, Sesion, SesionCurso, Semana, Horario, HorarioCurso,\
    Interesado, Descuento
# Register your models here.


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoria']
    search_fields = ['cateoria']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'curso', 'duracion', 'precio', 'id_categoria', 'url']
    search_fields = ['curso']

@admin.register(CursoDetalle)
class CursoDetalleAdmin(admin.ModelAdmin):
    list_display = ['id', 'curso_id', 'titulo', 'pregunta', 'descripcion']
    search_fields = ['curso-detalle']

@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ['id', 'sesion']
    search_fields = ['sesion']

@admin.register(SesionCurso)
class SesionCursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_curso', 'id_sesion']

@admin.register(Semana)
class SemanaAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_sesioncurso', 'semana', 'descripcion']
    search_fields = ['semana']

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'frecuencia', 'horaInicio', 'horaFin']
    search_fields = ['frecuencia']

@admin.register(HorarioCurso)
class HorarioCursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_curso', 'id_horario']

@admin.register(Beneficio)
class BeneficioAdmin(admin.ModelAdmin):
    list_display = ['id', 'beneficio']

@admin.register(Descuento)
class DescuentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo', 'status', 'interesado_id' ]

@admin.register(Interesado)
class InteresadoAdmin(admin.ModelAdmin):
    list_display = ['id','nombres', 'apellido_paterno', 'apellido_materno', 'celular', 'email' ]