# Generated by Django 3.2.8 on 2021-12-08 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='app_reg_usu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre de la app ')),
                ('descripcion', models.CharField(max_length=20, verbose_name='Descripcion ')),
                ('activo', models.BooleanField(default=False, verbose_name='Activo ')),
            ],
            options={
                'verbose_name': 'app_reg_usu',
                'verbose_name_plural': 'app_reg_usus',
            },
        ),
        migrations.CreateModel(
            name='curs_dict',
            fields=[
                ('id_cd', models.AutoField(primary_key=True, serialize=False)),
                ('instit', models.CharField(max_length=20, verbose_name='Nombre de la institucion académica donde dictó el curso. ')),
                ('tipo_form', models.IntegerField(choices=[(0, 'Universitaria'), (1, 'Especializacion'), (2, 'Maestría'), (3, 'Doctorado'), (4, 'PHD'), (5, 'Posdoctorado'), (6, 'Básica Secundaria'), (7, 'Básica Primaria'), (8, 'Diplomado'), (9, 'Curso Corto'), (10, 'Técnica'), (11, 'tecnológica'), (12, 'Curso libre')], default=0)),
                ('fch_ini', models.DateField(verbose_name='fecha de inicio')),
                ('fch_fin', models.DateField(verbose_name='fecha de fin')),
                ('certif', models.BooleanField(default=True, verbose_name='Posees Certificado')),
                ('nal', models.CharField(max_length=30, verbose_name='Pais ')),
                ('ciudad', models.CharField(max_length=30, verbose_name='Ciudad ')),
                ('mod', models.IntegerField(choices=[(0, 'Presencial'), (1, 'Virtual'), (2, 'Semipresencial'), (3, 'A distancia'), (4, 'Aprendizaje Acompañado')], default=0, verbose_name='Modalidad')),
                ('num_est', models.IntegerField(verbose_name='Cantidad de estudiantes')),
                ('dur', models.IntegerField(verbose_name='Número total de horas académicas del curso')),
                ('nom_curs', models.CharField(max_length=60, verbose_name='Nombre del curso')),
                ('mun_ciclos', models.IntegerField(verbose_name='cuántas veces se dictó el curso')),
                ('url_prog', models.URLField(verbose_name='Url del documento o sitio web ')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'curs_dict',
                'verbose_name_plural': 'curs_dicts',
            },
        ),
        migrations.CreateModel(
            name='discapacidad',
            fields=[
                ('id_disc', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_disca', models.CharField(max_length=30, verbose_name='Tipo de discapacidad ')),
                ('desc_disca', models.CharField(max_length=30, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'discapacidad',
                'verbose_name_plural': 'discapacidads',
            },
        ),
        migrations.CreateModel(
            name='form_acad',
            fields=[
                ('id_fa', models.AutoField(primary_key=True, serialize=False)),
                ('instit', models.CharField(max_length=25, verbose_name='Nombre de la institucion ')),
                ('tipo_form', models.IntegerField(choices=[(0, 'Universitaria'), (1, 'Especializacion'), (2, 'Maestría'), (3, 'Doctorado'), (4, 'PHD'), (5, 'Posdoctorado'), (6, 'Básica Secundaria'), (7, 'Básica Primaria'), (8, 'Diplomado'), (9, 'Curso Corto'), (10, 'Técnica'), (11, 'tecnológica'), (12, 'Curso libre')], default=0)),
                ('fch_ini', models.DateField(verbose_name='fecha de Inicio')),
                ('fch_fin', models.DateField(verbose_name='fecha de Fin')),
                ('certif', models.BooleanField(default=False, verbose_name='Posees Certificado')),
                ('nal', models.CharField(max_length=20, verbose_name='Pais ')),
                ('ciudad', models.CharField(max_length=20, verbose_name='Ciudad ')),
                ('mod', models.IntegerField(choices=[(0, 'Presencial'), (1, 'Virtual'), (2, 'Semipresencial'), (3, 'A distancia'), (4, 'Aprendizaje Acompañado')], default=0)),
                ('tit', models.CharField(max_length=20, verbose_name='Titulo obtenido ')),
                ('menc', models.CharField(max_length=20, verbose_name='Mensión ')),
                ('token', models.CharField(max_length=20, verbose_name='token de validación ')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'form_acad',
                'verbose_name_plural': 'form_acads',
            },
        ),
        migrations.CreateModel(
            name='habilidades',
            fields=[
                ('id_hab', models.AutoField(primary_key=True, serialize=False)),
                ('nom_hab', models.CharField(max_length=20, verbose_name='Nombre de la habilidad')),
                ('desc', models.CharField(max_length=20, verbose_name='Descripción de la Habilidad')),
            ],
            options={
                'verbose_name': 'habilidades',
                'verbose_name_plural': 'habilidadess',
            },
        ),
        migrations.CreateModel(
            name='red_soc',
            fields=[
                ('id_red', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_red', models.CharField(max_length=30, verbose_name='Dirección de Oficina (país, ciudad, dir) ')),
                ('usuario', models.CharField(max_length=20, verbose_name='Direcció n de Oficina (país, ciudad, dir) ')),
                ('url', models.URLField(verbose_name='Url de página principal dentro de la red.')),
                ('uso', models.CharField(max_length=20, verbose_name='Uso de la red (frecuente:0; moderado:1; poco frecuente:2; inactivo:3) ')),
                ('pub', models.BooleanField(default=False, verbose_name='acceso público de información de red')),
            ],
            options={
                'verbose_name': 'red_soc',
                'verbose_name_plural': 'red_socs',
            },
        ),
        migrations.CreateModel(
            name='valid_hab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_esc', models.CharField(max_length=20, verbose_name='IDENTIFICADOR ')),
                ('val', models.CharField(max_length=20, verbose_name='RANGO ')),
                ('id_hab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusu.habilidades')),
                ('id_usu_val', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'valid_hab',
                'verbose_name_plural': 'valid_habs',
            },
        ),
        migrations.CreateModel(
            name='usu_inf_prof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof', models.CharField(max_length=20, verbose_name='Titulo obtenido ')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'usu_inf_prof',
                'verbose_name_plural': 'usu_inf_profs',
            },
        ),
        migrations.CreateModel(
            name='usu_inf_pers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nuip', models.CharField(max_length=30, verbose_name='número único de identificación personal ')),
                ('tipo_nuip', models.IntegerField(choices=[(0, 'Cédula de Ciudadanía'), (1, 'Tarjeta de Identidad'), (2, 'Cédula de Extranjería'), (3, 'Pasaporte'), (4, 'Permiso de Residencia')], default=0)),
                ('nombres', models.CharField(max_length=60, verbose_name='Nombres ')),
                ('apelllidos', models.CharField(max_length=60, verbose_name='Apellidos ')),
                ('nal', models.CharField(max_length=30, verbose_name='Nacionalidad ')),
                ('fch_naci', models.DateField(verbose_name='fecha de nacimiento')),
                ('gene', models.IntegerField(choices=[(0, 'Neutro'), (1, 'Femenino'), (2, 'Masculino'), (3, 'Intergénero'), (4, 'Transgénero'), (5, 'Sisgénero'), (6, 'Otro')], default=0)),
                ('ocup', models.CharField(max_length=30, verbose_name='Ocupacion ')),
                ('dir', models.CharField(max_length=100, verbose_name='Direccion ')),
                ('discap', models.BooleanField(default=False, verbose_name='¿Es una persona en condición de discapacidad?')),
                ('url_imag', models.URLField(verbose_name='url de la imagen personal.')),
                ('zona_hor', models.CharField(max_length=100, verbose_name='Zona Horaria ')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo_discap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusu.discapacidad')),
            ],
            options={
                'verbose_name': 'usu_inf_pers',
                'verbose_name_plural': 'usu_inf_perss',
            },
        ),
        migrations.CreateModel(
            name='usu_inf_contac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind_nal', models.PositiveSmallIntegerField(verbose_name='Indicativo telefónico de país')),
                ('cel', models.CharField(max_length=30, verbose_name='Número de telefono móvil del usuario')),
                ('wa', models.CharField(max_length=30, verbose_name='Número de WhatsApp')),
                ('email', models.EmailField(max_length=30, verbose_name='Correo electrocico')),
                ('cod_post', models.PositiveSmallIntegerField(verbose_name='Número de código postal')),
                ('ls_ha', models.IntegerField(choices=[(0, '8am 12pm'), (1, '2pm 6pm'), (2, '8am 12pm - 2pm 6pm')], default=0)),
                ('web', models.URLField(verbose_name='dirección de página web o blog personal')),
                ('dir_offi', models.CharField(max_length=100, verbose_name='Dirección de Ofiina (país, ciudad, dir) ')),
                ('id_usu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'usu_inf_contac',
                'verbose_name_plural': 'usu_inf_contacs',
            },
        ),
        migrations.CreateModel(
            name='usu_inf_apps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'usu_inf_apps',
                'verbose_name_plural': 'usu_inf_appss',
            },
        ),
        migrations.CreateModel(
            name='usu_inf_acad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivelform', models.IntegerField(choices=[(0, 'Universitaria'), (1, 'Especializacion'), (2, 'Maestría'), (3, 'Doctorado'), (4, 'PHD'), (5, 'Posdoctorado'), (6, 'Básica Secundaria'), (7, 'Básica Primaria'), (8, 'Diplomado'), (9, 'Curso Corto'), (10, 'Técnica'), (11, 'tecnológica'), (12, 'Curso libre')], default=0)),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'usu_inf_acad',
                'verbose_name_plural': 'usu_inf_acads',
            },
        ),
        migrations.CreateModel(
            name='rl_usu_inf_red_social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ls_red', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusu.red_soc')),
            ],
            options={
                'verbose_name': 'rl_usu_inf_red_social',
                'verbose_name_plural': 'rl_usu_inf_red_socials',
            },
        ),
        migrations.CreateModel(
            name='rl_usu_inf_prof_empleos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ls_curs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusu.curs_dict')),
            ],
        ),
        migrations.CreateModel(
            name='rl_usu_inf_hab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=20, verbose_name='Descripción ')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ls_habs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusu.habilidades')),
            ],
            options={
                'verbose_name': 'rl_usu_inf_hab',
                'verbose_name_plural': 'rl_usu_inf_habs',
            },
        ),
        migrations.CreateModel(
            name='rl_usu_inf_form_acad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ls_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusu.form_acad')),
            ],
            options={
                'verbose_name': 'rl_usu_inf_form_acad',
                'verbose_name_plural': 'rl_usu_inf_form_acads',
            },
        ),
        migrations.CreateModel(
            name='rl_usu_inf_contac_curs_dict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ls_cursdict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusu.curs_dict')),
            ],
        ),
        migrations.CreateModel(
            name='rl_usu_inf_apps_rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'rl_usu_inf_apps_rol',
                'verbose_name_plural': 'rl_usu_inf_apps_rols',
            },
        ),
        migrations.CreateModel(
            name='empleos',
            fields=[
                ('id_empl', models.AutoField(primary_key=True, serialize=False)),
                ('instit', models.CharField(max_length=20, verbose_name='Nombre de la institucion ')),
                ('nom_cargo', models.CharField(max_length=20, verbose_name='Nombre del Cargo ')),
                ('fch_ini', models.DateField(verbose_name='fecha de inicio')),
                ('fch_fin', models.DateField(verbose_name='fecha de Fin')),
                ('certif', models.BooleanField(default=False, verbose_name='Posees certificado')),
                ('nal', models.CharField(max_length=20, verbose_name='Pais ')),
                ('ciudad', models.CharField(max_length=20, verbose_name='Ciudad ')),
                ('tipo_contr', models.IntegerField(choices=[(0, 'Término Indefinido'), (1, 'Término Fijo'), (2, 'Temporal'), (3, 'Orden de Servicio'), (4, 'Contrato de Obra'), (5, 'Asesoría'), (6, 'Consultoría'), (7, 'independiente')], default=0)),
                ('tit', models.CharField(max_length=20, verbose_name='Titulo obtenido ')),
                ('menc', models.CharField(max_length=20, verbose_name='Mensión de honor ')),
                ('token', models.CharField(max_length=20, verbose_name='Token de validación electrónica  ')),
                ('ret', models.CharField(max_length=20, verbose_name=' Motivo del retiro ')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'empleos',
                'verbose_name_plural': 'empleoss',
            },
        ),
    ]
