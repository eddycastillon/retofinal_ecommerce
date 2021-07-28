from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

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
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.curso}'

    class Meta:
        db_table = 'courses'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']


class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    frecuencia = models.CharField(max_length=50)
    horaInicio = models.CharField(max_length=12)
    horaFin = models.CharField(max_length=12)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

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
    update_at = models.DateTimeField(auto_now_add=True)

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
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sesion}'

    class Meta:
        db_table = 'sesiones'
        verbose_name = 'Sesion'
        verbose_name_plural = 'Sesiones'
        ordering = ['sesion']


class Semana(models.Model):
    id = models.AutoField(primary_key=True)
    id_sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE)
    semana = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.semana}'
    
    class Meta:
        db_table = 'semanas'
        verbose_name = 'Semana'
        verbose_name_plural = 'Semanas'
        ordering = ['semana']
