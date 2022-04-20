# Generated by Django 3.2.8 on 2022-04-19 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_regusu', '0001_initial'),
        ('App_modadm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_regusugr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='conv_inv',
            fields=[
                ('id_conv', models.AutoField(primary_key=True, serialize=False)),
                ('val_min', models.IntegerField()),
                ('val_max', models.IntegerField()),
                ('fch_ini', models.DateField(verbose_name='Fecha de inicio Incripciones: ')),
                ('fch_fin', models.DateField(verbose_name='Fecha de Cierre de Inscripciones: ')),
                ('pltf', models.BooleanField(default=False, verbose_name='Se puede registrar desde la plataforma: ')),
                ('nal', models.CharField(max_length=30, verbose_name='Pais ')),
                ('ciudad', models.CharField(max_length=30, verbose_name='Ciudad ')),
                ('mod', models.IntegerField(choices=[(0, 'Presencial'), (1, 'Virtual'), (2, 'Semipresencial'), (3, 'A distancia'), (4, 'Aprendizaje Acompañado')], default=0, verbose_name='Modalidad ')),
                ('und_acdm', models.CharField(max_length=60, verbose_name='Nombre de la unidad académica ')),
                ('resp', models.CharField(max_length=60, verbose_name='Nombre de la persona responsable ')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo ')),
                ('nom_conv', models.CharField(max_length=60, verbose_name='Nombre de la convocatori ')),
                ('url_conv', models.URLField(max_length=80, verbose_name='sitio web donde se puede localizar los términos de al convocatoria')),
                ('url_insc', models.URLField(max_length=80, verbose_name='Url del formulario de inscripción')),
            ],
            options={
                'verbose_name': 'conv_inv',
                'verbose_name_plural': 'conv_invs',
            },
        ),
        migrations.CreateModel(
            name='prog_ofer',
            fields=[
                ('id_prog', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_form', models.IntegerField(choices=[(0, 'Universitaria'), (1, 'Especializacion'), (2, 'Maestría'), (3, 'Doctorado'), (4, 'PHD'), (5, 'Posdoctorado'), (6, 'Básica Secundaria'), (7, 'Básica Primaria'), (8, 'Diplomado'), (9, 'Curso Corto'), (10, 'Técnica'), (11, 'tecnológica'), (12, 'Curso libre')], default=0)),
                ('fch_ini', models.DateField(verbose_name='fecha de inscripcion')),
                ('fch_fin', models.DateField(verbose_name='fecha de Cierre de la inscripcion')),
                ('certif', models.BooleanField(default=True, verbose_name='Posee certificado')),
                ('nal', models.CharField(max_length=30, verbose_name='Pais: ')),
                ('ciudad', models.CharField(max_length=40, verbose_name='Ciudad ')),
                ('mod', models.IntegerField(choices=[(0, 'Presencial'), (1, 'Virtual'), (2, 'Semipresencial'), (3, 'A distancia'), (4, 'Aprendizaje Acompañado')], default=0, verbose_name='MODALIDAD')),
                ('num_est', models.PositiveSmallIntegerField(default=5, verbose_name='cantidad d estudiantes ')),
                ('dur', models.PositiveSmallIntegerField(default=4, verbose_name='Número total de horas')),
                ('dur_sem', models.PositiveSmallIntegerField(default=4, verbose_name='Número total de semestres')),
                ('nom_prog', models.CharField(max_length=30, verbose_name='Nombre del Programa')),
                ('acred', models.BooleanField(default=True, verbose_name='El programa se encuentra acreditado')),
                ('ven_acrd', models.PositiveSmallIntegerField(default=5, verbose_name='Año de vencimiento de la acreditación')),
                ('url_prog', models.URLField(max_length=80, verbose_name='sitio web donde se puede localizar el programa')),
            ],
            options={
                'verbose_name': 'prog_ofer',
                'verbose_name_plural': 'prog_ofers',
            },
        ),
        migrations.CreateModel(
            name='usui',
            fields=[
                ('id_usuinst', models.AutoField(primary_key=True, serialize=False)),
                ('passinst', models.CharField(max_length=15, verbose_name='Contraseña ')),
                ('fch_regi', models.DateField(verbose_name='fecha de registro de usurio: ')),
                ('activo', models.BooleanField(default=True, verbose_name=' estatus del usuario activo')),
                ('id_rol_app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.rol')),
                ('id_usu_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'usui',
                'verbose_name_plural': 'usuis',
            },
        ),
        migrations.CreateModel(
            name='usui_inf_inst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nuii', models.CharField(max_length=30, verbose_name='número único de identificación institucional sin puntos')),
                ('tipo_nuii', models.IntegerField(choices=[(0, 'NIT'), (1, 'RUT')], default=0, verbose_name='Tipo de Número de identificación Institucional')),
                ('rs', models.CharField(max_length=30, verbose_name='Razón Social de la Institución')),
                ('sigla', models.CharField(max_length=20, verbose_name='Sigla institucional')),
                ('repleg', models.CharField(max_length=60, verbose_name='Nombre Completo del representante legal')),
                ('nal', models.CharField(max_length=25, verbose_name='nacionalidad')),
                ('fch_ini', models.DateField(verbose_name='fecha de inicio de la institución')),
                ('fch_reg', models.DateField(verbose_name='fecha de registro de la institución en al plataforma')),
                ('tipo_inst', models.IntegerField(choices=[('Cédula', 'Cédula'), ('Tarjeta de identidad', 'Tarjeta de identidad'), ('Cédula de Extranjería', 'Cédula de Extranjería'), ('Pasaporte', 'Pasaporte'), ('Permiso de Residencia', 'Permiso de Residencia')], default=0, verbose_name='Tipo de institución o entidad')),
                ('sector', models.IntegerField(choices=[(0, 'Privado'), (1, 'Publico'), (2, 'xxx'), (3, 'zzzz')], default=0, verbose_name='sector de desempeño de la entidad o institución ')),
                ('dir', models.TextField(verbose_name='direccion sede administrativa')),
                ('url_imag', models.URLField(verbose_name='url de la imagen institucional o logo')),
                ('zona_hor', models.CharField(max_length=60, verbose_name='Zona Horario internacional')),
                ('id_usui', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.usui')),
            ],
            options={
                'verbose_name': 'usui_inf_inst',
                'verbose_name_plural': 'usui_inf_insts',
            },
        ),
        migrations.CreateModel(
            name='usui_inf_contac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind_nal', models.CharField(max_length=5, verbose_name='Indicativo telefónico de país')),
                ('tel', models.CharField(max_length=20, verbose_name='Número de telefono fijo')),
                ('cel', models.CharField(max_length=20, verbose_name='Número de telefono móvil')),
                ('email', models.EmailField(max_length=40, verbose_name='correo ')),
                ('cod_post', models.PositiveSmallIntegerField(default=8, verbose_name='código postal ')),
                ('ls_ha', models.IntegerField(choices=[(0, '8am 12pm'), (1, '2pm 6pm'), (2, '8am 12pm - 2pm 6pm')], default=0)),
                ('web', models.URLField(max_length=60, verbose_name=' dirección de página web o blog institucional')),
                ('dir_pri', models.TextField(verbose_name='Dirección de sede principal (país, ciudad, dir. ')),
                ('id_usui', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.usui')),
            ],
            options={
                'verbose_name': 'usui_inf_contac',
                'verbose_name_plural': 'usui_inf_contacs',
            },
        ),
        migrations.CreateModel(
            name='usui_inf_apps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usui', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.usui')),
                ('rol_sis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.rol')),
            ],
            options={
                'verbose_name': 'usui_inf_apps',
                'verbose_name_plural': 'usui_inf_appss',
            },
        ),
        migrations.CreateModel(
            name='rl_usuo_prog_ofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_prog_ofer', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='App_regusui.prog_ofer')),
                ('id_usui', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.usui')),
            ],
            options={
                'verbose_name': 'rl_usuo_prog_ofer',
                'verbose_name_plural': 'rl_usuo_prog_ofers',
            },
        ),
        migrations.CreateModel(
            name='rl_usui_usugr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usui', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.usui')),
                ('ls_usugr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr')),
            ],
        ),
        migrations.CreateModel(
            name='rl_usui_usu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usui', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.usui')),
                ('ls_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='rl_usui_rol_actual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usui', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.usui')),
                ('rol_sis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.rol')),
            ],
        ),
        migrations.CreateModel(
            name='rl_usui_red_social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_red_social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusu.red_soc')),
                ('id_usui', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.usui')),
            ],
            options={
                'verbose_name': 'rl_usui_red_social',
                'verbose_name_plural': 'rl_usui_red_socials',
            },
        ),
        migrations.CreateModel(
            name='rl_usui_inf_acad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivelform', models.IntegerField(choices=[(0, 'Universitaria'), (1, 'Especializacion'), (2, 'Maestría'), (3, 'Doctorado'), (4, 'PHD'), (5, 'Posdoctorado'), (6, 'Básica Secundaria'), (7, 'Básica Primaria'), (8, 'Diplomado'), (9, 'Curso Corto'), (10, 'Técnica'), (11, 'tecnológica'), (12, 'Curso libre')], default=0, verbose_name='Nivel de formacion ')),
                ('id_usui', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.usui')),
            ],
            options={
                'verbose_name': 'usui_inf_acad',
                'verbose_name_plural': 'usui_inf_acads',
            },
        ),
        migrations.CreateModel(
            name='rl_usui_conv_inv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usui', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.usui')),
                ('ls_conv_inv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.conv_inv')),
            ],
        ),
        migrations.AddField(
            model_name='prog_ofer',
            name='id_usui',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.usui'),
        ),
        migrations.AddField(
            model_name='conv_inv',
            name='id_usui',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusui.usui'),
        ),
        migrations.CreateModel(
            name='app_reg_ins',
            fields=[
                ('app_reg_ins', models.AutoField(primary_key=True, serialize=False)),
                ('nomb_app_reg_ins', models.CharField(max_length=20, verbose_name='Nombre  ')),
                ('desc_app_reg_ins', models.CharField(max_length=20, verbose_name='Descripcion  ')),
                ('status_app_reg_ins', models.BooleanField(default=False, verbose_name='Activo ')),
                ('id_aplicacion_administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.mod')),
            ],
            options={
                'verbose_name': 'app_reg_ins',
                'verbose_name_plural': 'app_reg_inss',
            },
        ),
    ]
