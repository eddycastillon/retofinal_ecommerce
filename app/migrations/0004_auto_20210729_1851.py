# Generated by Django 3.2.5 on 2021-07-29 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210729_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semana',
            name='id_sesion',
        ),
        migrations.AddField(
            model_name='semana',
            name='id_SesionCurso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.sesioncurso'),
        ),
    ]
