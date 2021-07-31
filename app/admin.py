from re import search
from django.contrib import admin
from .models import Beneficio, Categoria, Curso, CursoBeneficio, Sesion, SesionCurso, Semana, Horario, HorarioCurso
# Register your models here.


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoria']
    search_fields = ['cateoria']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'curso', 'duracion', 'precio', 'id_categoria', 'url']
    search_fields = ['curso']

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

@admin.register(CursoBeneficio)
class CursoBeneficioAdmin(admin.ModelAdmin):
    list_display = ['id', 'curso', 'beneficio']