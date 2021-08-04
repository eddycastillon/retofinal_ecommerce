# Generated by Django 3.2.5 on 2021-08-04 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_descuento_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoDetalle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('pregunta', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('curso_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
            ],
        ),
    ]
