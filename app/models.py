from rest_framework.fields import ReadOnlyField
import shortuuid
from django.db import models
from django.db.models.fields import AutoField, UUIDField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.categoria}'

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

        
class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=255)
    duracion = models.IntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=5)
    id_categoria = ForeignKey(Categoria, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.curso}'

    class Meta:
        db_table = 'courses'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

class CursoDetalle(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    pregunta  = models.CharField(max_length=255)
    descripcion = models.TextField()
    curso_id = ForeignKey(Curso, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.titulo}'

    class Meta:
        db_table = 'curso_detalle'
        verbose_name = 'Curso Detalle'
        verbose_name_plural = 'Cursos Detalles'
        ordering = ['id']

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    frecuencia = models.CharField(max_length=50)
    horaInicio = models.CharField(max_length=12)
    horaFin = models.CharField(max_length=12)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.frecuencia} {self.horaInicio} - {self.horaFin}'

    class Meta:
        db_table = 'horarios'
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['frecuencia']


class HorarioCurso(models.Model):
    id = models.AutoField(primary_key=True)
    id_horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id_horario}-{self.id_curso}'

    class Meta:
        db_table = 'horario_curso'
        verbose_name = 'Horario de Curso'
        verbose_name_plural = 'Horario de Cursos'
        ordering = ['id']


class Sesion(models.Model):
    id = models.AutoField(primary_key=True)
    sesion = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sesion}'

    class Meta:
        db_table = 'sesiones'
        verbose_name = 'Sesion'
        verbose_name_plural = 'Sesiones'
        ordering = ['sesion']


class SesionCurso(models.Model):
    id = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id_curso} - {self.id_sesion}'
    
    class Meta:
        db_table = 'sesion_cursos'
        verbose_name = 'Sesion de Curso'
        verbose_name_plural = 'Sesion de Cursos'


class Semana(models.Model):
    id = models.AutoField(primary_key=True)
    id_sesioncurso = models.ForeignKey(SesionCurso, on_delete=models.CASCADE, null=True)
    semana = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.semana}'
    
    class Meta:
        db_table = 'semanas'
        verbose_name = 'Semana'
        verbose_name_plural = 'Semanas'
        ordering = ['semana']



class Beneficio(models.Model):
    id = models.AutoField(primary_key=True)
    beneficio = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.beneficio}'

    class Meta:
        db_table = 'beneficios'
        verbose_name = 'Beneficio'
        verbose_name_plural = 'Beneficios'
        ordering = ['id']



class Interesado(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombres}'

    class Meta:
        db_table = 'interesados'
        verbose_name = 'Interesado'
        verbose_name_plural = 'Interesados'
        ordering = ['id']


class Descuento(models.Model):

    id = models.AutoField(primary_key=True)
    #codigo = models.CharField(max_length=255)
    codigo = models.CharField(unique=True,  max_length=10, editable=False)
    status = models.BooleanField(default=True)
    interesado_id = ForeignKey(Interesado, on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.codigo}'

    class Meta:
        db_table = 'descuentos'
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'
        ordering = ['id']


