# Generated by Django 3.2.8 on 2021-12-08 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_modadm', '0001_initial'),
        ('App_regusu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='app_reg_gr',
            fields=[
                ('id_app_reg_gr', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=40, verbose_name='Descripcion.')),
            ],
            options={
                'verbose_name': 'app_reg_gr',
                'verbose_name_plural': 'app_reg_grs',
            },
        ),
        migrations.CreateModel(
            name='curs_ofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instit', models.CharField(max_length=20, verbose_name='Nombre de la institucion académica ')),
                ('tipo_form_gr', models.IntegerField(choices=[(0, 'Seminario'), (1, 'Taller'), (2, 'Foro'), (3, 'Charla'), (4, 'Encuentro'), (5, 'Simposio'), (6, 'Panel'), (7, 'Conferencia'), (8, 'Diplomado'), (9, 'Curso Corto'), (10, 'Congreso'), (11, 'Socialización'), (12, 'Coloquio'), (13, 'Otro')], default=0)),
                ('fch_ini', models.DateField(verbose_name='fecha Inicio')),
                ('fch_fin', models.DateField(verbose_name='fecha Fin ')),
                ('certif', models.BooleanField(default=True, verbose_name='Activo ')),
                ('nal', models.CharField(max_length=30, verbose_name='Pais: ')),
                ('ciudad', models.CharField(max_length=30, verbose_name='Ciudad ')),
                ('mod', models.IntegerField(choices=[(0, 'Presencial'), (1, 'Virtual'), (2, 'Semipresencial'), (3, 'A distancia'), (4, 'Aprendizaje Acompañado')], default=0)),
                ('num_est', models.PositiveSmallIntegerField(default=5, verbose_name='Cupo de Estudiantes o asistentes')),
                ('dur', models.PositiveSmallIntegerField(default=5, verbose_name='Número total de horas académicas del curso')),
                ('nom_curs', models.CharField(max_length=30, verbose_name='Nombre del Curso o evento académico. ')),
                ('mun_ciclos', models.PositiveSmallIntegerField(default=5, verbose_name='cuántas veces se realizará el curso o evento')),
                ('url_prog', models.URLField(verbose_name='página web o blog del grupo ')),
                ('inscr', models.URLField(null='False', verbose_name='Url del formulario de inscripción.')),
            ],
            options={
                'verbose_name': 'curs_ofer',
                'verbose_name_plural': 'curs_ofers',
            },
        ),
        migrations.CreateModel(
            name='etapa_gr',
            fields=[
                ('id_etp_gr', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20, verbose_name='Nombre del grupo  ')),
                ('fch_ini_nom', models.DateField(verbose_name='Fecha en la que se creó el grupo ')),
                ('fch_fin_nom', models.DateField(verbose_name='Fecha en la que se terminó el grupo')),
                ('vig', models.BooleanField(default=True, verbose_name='El nombre se encuentra vigente ')),
                ('sigla', models.CharField(max_length=20, verbose_name='Sigla con la que se identificó(a) el grupo ')),
                ('url_arch', models.URLField(verbose_name='URL del sitio web ')),
                ('gruplac', models.URLField(blank='False', null='False', verbose_name='Url del GrupLac del grupo de Investigación con ese nombre si se está registrado en esa plataforma.')),
            ],
            options={
                'verbose_name': 'etapa_gr',
                'verbose_name_plural': 'etapa_grs',
            },
        ),
        migrations.CreateModel(
            name='form_acad_gr',
            fields=[
                ('id_form_acad_gr', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_form', models.IntegerField(choices=[(0, 'Seminario'), (1, 'Taller'), (2, 'Foro'), (3, 'Charla'), (4, 'Encuentro'), (5, 'Simposio'), (6, 'Panel'), (7, 'Conferencia'), (8, 'Diplomado'), (9, 'Curso Corto'), (10, 'Congreso'), (11, 'Socialización'), (12, 'Coloquio'), (13, 'Otro')], default=0)),
                ('fch_ini', models.DateField(verbose_name='Fecha de inicio ')),
                ('fch_fin', models.DateField(verbose_name='Fecha de fin: ')),
                ('certif', models.BooleanField(default=True, verbose_name='Posees Ceertificado: ')),
                ('nal', models.CharField(max_length=25, verbose_name='Pais ')),
                ('ciudad', models.CharField(max_length=25, verbose_name='Ciudad: ')),
                ('mod', models.IntegerField(choices=[(0, 'Presencial'), (1, 'Virtual'), (2, 'Semipresencial'), (3, 'A distancia'), (4, 'Aprendizaje Acompañado')], default=0)),
                ('asis', models.PositiveSmallIntegerField(default=5, verbose_name='Número de asistentes')),
                ('hora', models.PositiveSmallIntegerField(default=5, verbose_name=' Número de horas académicas')),
                ('mem', models.URLField(verbose_name='url de las memorias del tipo de formación')),
                ('token', models.CharField(max_length=30, verbose_name='Token de validación electrónica')),
            ],
            options={
                'verbose_name': 'form_acad_gr',
                'verbose_name_plural': 'form_acad_gr',
            },
        ),
        migrations.CreateModel(
            name='usu_nr',
            fields=[
                ('id_usu_nr', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=40, verbose_name='Nombres del integrante no registrado(a).')),
                ('apellidos', models.CharField(max_length=40, verbose_name='Apellidos del integrante no registrado(a).')),
                ('cvlac', models.URLField(verbose_name='URL del CVlac del investigador(a).')),
                ('orcid', models.CharField(max_length=20, verbose_name='ID de ORCID del investigador(a).')),
                ('ggl', models.URLField(verbose_name='URL Google académico del investigador(a)')),
            ],
            options={
                'verbose_name': 'usu_nr',
                'verbose_name_plural': 'usu_nrs',
            },
        ),
        migrations.CreateModel(
            name='usugr',
            fields=[
                ('id_gr', models.AutoField(primary_key=True, serialize=False)),
                ('passgr', models.CharField(max_length=20, verbose_name='Descripcion ')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo ')),
                ('id_rol_app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App_modadm.rol')),
                ('id_usu_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'usugr',
                'verbose_name_plural': 'usugr',
            },
        ),
        migrations.CreateModel(
            name='usugr_inf_gr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_gr', models.PositiveSmallIntegerField(default=8, verbose_name=' código único de identificación del grupo')),
                ('tipo_gr', models.IntegerField(choices=[(0, 'Independiente'), (1, 'Reconocido Inst'), (2, 'Reconocido COLC'), (3, 'Semillero de Inv.'), (4, 'Comunidad'), (5, 'Estado del Arte')], default=0)),
                ('nal', models.CharField(max_length=40, verbose_name='Nacionalidad')),
                ('dir', models.CharField(max_length=40, verbose_name='Direccion de correspondencia ')),
                ('estado', models.IntegerField(choices=[(0, 'Creado'), (1, 'Desarrollo Temprano'), (2, 'Dearrollo Medio'), (3, 'Desarrollo Alto'), (4, 'Consolidado'), (5, 'Ramificado'), (6, 'Fusionado'), (7, 'Disgregado'), (8, 'Disuelto'), (9, 'liquidado'), (10, 'Abandonado')], default=0)),
                ('url_imag', models.URLField(verbose_name='url de la imagen o logo del grupo')),
                ('zona_hor', models.CharField(max_length=40, verbose_name='Zona Horaria')),
                ('id_gr_padre', models.CharField(default=0, max_length=40, verbose_name='grupo padre')),
                ('id_etp_gr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.etapa_gr')),
                ('id_usugr', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr')),
            ],
            options={
                'verbose_name': 'usugr_inf_gr',
                'verbose_name_plural': 'usugr_inf_grs',
            },
        ),
        migrations.CreateModel(
            name='usugr_inf_red_social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usugr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr_inf_gr')),
                ('ls_red', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusu.red_soc')),
            ],
        ),
        migrations.CreateModel(
            name='usugr_inf_contac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind_nal', models.CharField(max_length=20, verbose_name='Nacionalidad ')),
                ('tel', models.CharField(max_length=20, verbose_name='Telefono oficina ')),
                ('cel', models.CharField(max_length=20, verbose_name='N° Celular ')),
                ('email', models.EmailField(max_length=254, verbose_name='correo')),
                ('cod_post', models.IntegerField(verbose_name='Codigo Postal ')),
                ('ls_hr', models.IntegerField(choices=[(0, '8am 12pm'), (1, '2pm 6pm'), (2, '8am 12pm - 2pm 6pm')], default=0)),
                ('web', models.URLField(verbose_name='página web o blog del grupo ')),
                ('dir_offi', models.TextField(verbose_name='Direccion e oficina')),
                ('id_usugr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr')),
            ],
            options={
                'verbose_name': 'usugr_inf_contac',
                'verbose_name_plural': 'usugr_inf_contacs',
            },
        ),
        migrations.CreateModel(
            name='usugr_inf_apps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usugr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr')),
            ],
            options={
                'verbose_name': 'usugr_inf_apps',
                'verbose_name_plural': 'usugr_inf_appss',
            },
        ),
        migrations.CreateModel(
            name='rl_usugr_inf_rol_Actual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usugr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr')),
            ],
        ),
        migrations.CreateModel(
            name='rl_usugr_form_acad_gr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usugr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr_inf_gr')),
                ('ls_form_gr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.form_acad_gr')),
            ],
        ),
        migrations.CreateModel(
            name='rl_usugr_curs_ofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usugr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr_inf_gr')),
                ('ls_cursofer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.curs_ofer')),
            ],
        ),
        migrations.CreateModel(
            name='rel_usugr_ls_usu_nr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_gr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr')),
                ('ls_int_nr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usu_nr')),
            ],
            options={
                'verbose_name': 'rel_usugr_ls_usu_nr',
                'verbose_name_plural': 'rel_usugr_ls_usu_nrs',
            },
        ),
        migrations.CreateModel(
            name='rel_usugr_ls_usu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_gr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr')),
                ('ls_int_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'rel_usugr_ls_usu',
                'verbose_name_plural': 'rel_usugr_ls_usus',
            },
        ),
        migrations.CreateModel(
            name='rel_usugr_ls_etp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_gr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr')),
                ('ls_etp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.etapa_gr')),
            ],
            options={
                'verbose_name': 'rel_usugr_ls_etp',
                'verbose_name_plural': 'rel_usugr_ls_etps',
            },
        ),
    ]
