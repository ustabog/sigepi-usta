# Generated by Django 3.2 on 2022-06-09 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_regpry', '__first__'),
        ('app_recur', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='acti',
            fields=[
                ('id_activ', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_acti', models.CharField(max_length=255, verbose_name='Nombre de la actividad:')),
                ('desc_acti', models.CharField(max_length=255, verbose_name='Descripción de la actividad:')),
                ('fch_ini_acti', models.DateField(verbose_name='Fecha de inicio de la actividad')),
                ('fch_fin_acti', models.DateField(verbose_name='Fecha de finalización de la actividad')),
                ('url_acti', models.URLField(verbose_name='URL de la evidencia de la actividad')),
                ('id_pry_base', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_regpry.pry_base')),
                ('id_recurso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_recur.recu_pry')),
                ('id_usu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'actividad',
                'verbose_name_plural': 'actividades',
            },
        ),
        migrations.CreateModel(
            name='tarea',
            fields=[
                ('id_tarea', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tarea', models.CharField(max_length=255, verbose_name='Nombre de la actividad:')),
                ('desc_tarea', models.CharField(max_length=255, verbose_name='Descripción de la actividad:')),
                ('fch_ini_tarea', models.DateField(verbose_name='Fecha de inicio de la tarea')),
                ('fch_fin_tarea', models.DateField(verbose_name='Fecha de finalización de la tarea')),
                ('url_tar', models.URLField(verbose_name='URL de la evidencia de la tarea')),
                ('acti', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_crono.acti')),
                ('id_pry_base', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_regpry.pry_base')),
                ('id_recurso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_recur.recu_pry')),
                ('id_usu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'tarea',
                'verbose_name_plural': 'tareas',
            },
        ),
        migrations.CreateModel(
            name='proceso',
            fields=[
                ('id_proceso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proc', models.CharField(max_length=255, verbose_name='Nombre del proceso:')),
                ('desc_proc', models.CharField(max_length=255, verbose_name='Descripción del proceso:')),
                ('fch_ini_proc', models.DateField(verbose_name='Fecha de inicio del proceso')),
                ('fch_fin_proc', models.DateField(verbose_name='Fecha de finalización del proceso')),
                ('tarea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_crono.tarea')),
            ],
            options={
                'verbose_name': 'proceso',
                'verbose_name_plural': 'procesos',
            },
        ),
        migrations.CreateModel(
            name='fase',
            fields=[
                ('id_fase', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_fase', models.CharField(max_length=255, verbose_name='Nombre del proceso:')),
                ('desc_fase', models.CharField(max_length=255, verbose_name='Descripción del proceso:')),
                ('fch_ini_fase', models.DateField(verbose_name='Fecha de inicio de la fase')),
                ('fch_fin_fase', models.DateField(verbose_name='Fecha de finalización de la fase')),
                ('proceso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_crono.proceso')),
            ],
            options={
                'verbose_name': 'fase',
                'verbose_name_plural': 'fases',
            },
        ),
        migrations.CreateModel(
            name='etapa',
            fields=[
                ('id_etapa', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_eta', models.CharField(max_length=255, verbose_name='Nombre del proceso:')),
                ('desc_eta', models.CharField(max_length=255, verbose_name='Descripción del proceso:')),
                ('fch_ini_eta', models.DateField(verbose_name='Fecha de inicio de la etapa')),
                ('fch_fin_eta', models.DateField(verbose_name='Fecha de finalización de la etapa')),
                ('fase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_crono.fase')),
            ],
            options={
                'verbose_name': 'etapa',
                'verbose_name_plural': 'etapas',
            },
        ),
        migrations.CreateModel(
            name='crono_pry',
            fields=[
                ('id_crono_pry', models.AutoField(primary_key=True, serialize=False)),
                ('nomb_crono', models.CharField(max_length=255, verbose_name='Nombre del cronograma:')),
                ('desc_crono', models.CharField(max_length=255, verbose_name='Descripción del cronograma:')),
                ('fch_ini_pry', models.DateField(verbose_name='Fecha de inicio del proyecto')),
                ('fch_fin_pry', models.DateField(verbose_name='Fecha de finalización del proyecto')),
                ('etapa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_crono.etapa')),
                ('nombre_pry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_regpry.pry_base')),
                ('resp_pry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'crono_pry',
                'verbose_name_plural': 'crono_prys',
            },
        ),
    ]
