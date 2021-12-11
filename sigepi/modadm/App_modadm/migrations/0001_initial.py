# Generated by Django 3.2.8 on 2021-12-11 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modadm.App_modadm.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app_mod',
            fields=[
                ('id_app', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=40, verbose_name='Título de la aplicacion: ')),
                ('desc', models.CharField(max_length=80, verbose_name='descricion de la aplicacion: ')),
                ('url_doc', models.URLField(verbose_name='Direción local a la documentación o manual de la aplicación')),
                ('version', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Versión de desarrollo de la aplicación: ')),
                ('ver_mod', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Versión de desarrollo de la aplicación: ')),
                ('activo', models.BooleanField(default=False, verbose_name='estatus de la aplicacion ')),
                ('instalada', models.BooleanField(default=False, verbose_name='¿La aplicación se encuentra instalada? ')),
                ('visible', models.BooleanField(default=False, verbose_name='¿Activa o desactiva la visibilidad de la aplicacion.?')),
            ],
            options={
                'verbose_name': 'app_mod',
                'verbose_name_plural': 'app_mods',
            },
        ),
        migrations.CreateModel(
            name='func_app',
            fields=[
                ('id_func', models.AutoField(primary_key=True, serialize=False)),
                ('nom_func', models.CharField(max_length=30, verbose_name='Nombre de la función: ')),
                ('lib_func', models.CharField(max_length=30, verbose_name='Librería que contiene la función: ')),
                ('url_loc', models.URLField(verbose_name='Direción local a la documentación o manual de la aplicación')),
                ('com_exc', models.CharField(max_length=20, verbose_name='Comando de Ejecución de la Función: ')),
                ('text', models.CharField(max_length=20, verbose_name='Nombre de Función: ')),
                ('context', models.CharField(max_length=20, verbose_name='Contexto: ')),
                ('activa', models.BooleanField(default=False, verbose_name='¿Activa o desactiva.?')),
                ('indice', models.IntegerField()),
            ],
            options={
                'verbose_name': 'func_app',
                'verbose_name_plural': 'func_apps',
            },
        ),
        migrations.CreateModel(
            name='listado_aplicativo',
            fields=[
                ('id_aplicativo', models.AutoField(primary_key=True, serialize=False)),
                ('nom_aplicativo', models.CharField(max_length=30, verbose_name='aplicativo nombre: ')),
                ('activoaplicativo', models.BooleanField(default=False, verbose_name='¿Activo o desactivo.?')),
            ],
            options={
                'verbose_name': 'listado_aplicativo',
                'verbose_name_plural': 'listado_aplicativo',
            },
        ),
        migrations.CreateModel(
            name='mod',
            fields=[
                ('id_mod', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=40, verbose_name='Título del módulo')),
                ('desc', models.CharField(max_length=50, verbose_name='descripcion del Módulo')),
                ('url_doc', models.URLField(verbose_name='url Documentación')),
                ('version', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Versión de desarrollo ')),
                ('activo', models.BooleanField(default=False, verbose_name='Activo')),
                ('instalado', models.BooleanField(default=False, verbose_name='¿el módulo se encuentra instalado?')),
                ('visible', models.BooleanField(default=False, verbose_name='¿Activa o desactiva la visibilidad de la aplicacion.?')),
                ('ls_param_cnf', models.CharField(default='0', max_length=100, verbose_name='Listado de parámetro de configuración')),
            ],
            options={
                'verbose_name': 'mod',
                'verbose_name_plural': 'mods',
            },
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('etq_rol', models.CharField(max_length=30, verbose_name='Etiqueta: ')),
                ('desc', models.CharField(max_length=30, verbose_name='Descripcion del Rol: ')),
                ('tipo', models.IntegerField(choices=[(0, 'Sistema'), (1, 'Módulo'), (2, 'Aplicación'), (3, 'Extensión'), (4, 'Otro')], default=0)),
                ('req_reg', models.BooleanField(default=False, verbose_name='¿Activa o desactiva.?')),
                ('id_app', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App_modadm.app_mod')),
                ('id_mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App_modadm.mod')),
            ],
            options={
                'verbose_name': 'rol',
                'verbose_name_plural': 'rols',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_usu', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombres')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=80)),
                ('phoneNumber', models.CharField(max_length=9, unique=True, verbose_name='Numero de telefono')),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer'), ('Ninguno', 'Ninguno')], max_length=7)),
                ('Is_Partner', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateField(auto_now=True)),
                ('last_login', models.DateTimeField(verbose_name=modadm.App_modadm.models.User.update_last_login)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='usu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombres')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=80)),
                ('fch_regi', models.DateField(verbose_name='fecha de registro')),
                ('activo', models.BooleanField(default=False, verbose_name='¿Activo o desactivado.?')),
                ('id_rol_sis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.rol')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'usu',
                'verbose_name_plural': 'usus',
            },
        ),
        migrations.CreateModel(
            name='rl_mod_rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.mod')),
                ('ls_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.rol')),
            ],
            options={
                'verbose_name': 'rl_mod_rol',
                'verbose_name_plural': 'rl_mod_rols',
            },
        ),
        migrations.CreateModel(
            name='rl_mod_func',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.mod')),
                ('ls_func', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.func_app')),
            ],
            options={
                'verbose_name': 'rl_mod_funcs',
                'verbose_name_plural': 'rl_mod_funcs',
            },
        ),
        migrations.CreateModel(
            name='rl_mod_app_mod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.mod')),
                ('ls_app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.app_mod')),
            ],
            options={
                'verbose_name': 'rl_mod_app_mod',
                'verbose_name_plural': 'rl_mod_app_mods',
            },
        ),
        migrations.CreateModel(
            name='rl_app_mod_rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='activo')),
                ('id_app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.app_mod')),
                ('ls_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.rol')),
            ],
            options={
                'verbose_name': 'rl_app_mod_rol',
                'verbose_name_plural': 'rl_app_mod_rols',
            },
        ),
        migrations.CreateModel(
            name='rl_app_mod_func',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.app_mod')),
                ('ls_func', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.func_app')),
            ],
            options={
                'verbose_name': 'rl_app_mod_func',
                'verbose_name_plural': 'rl_app_mod_funcs',
            },
        ),
        migrations.CreateModel(
            name='mod_adm',
            fields=[
                ('sesion', models.AutoField(primary_key=True, serialize=False)),
                ('id_mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.mod')),
                ('id_usu_adm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'mod_adm',
                'verbose_name_plural': 'mod_adms',
            },
        ),
        migrations.CreateModel(
            name='log_acc_pltf',
            fields=[
                ('id_acc_pltf', models.AutoField(primary_key=True, serialize=False)),
                ('fch_ini', models.DateField(verbose_name='fecha de inicio')),
                ('fch_fin', models.DateField(verbose_name='fecha de fin')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'log_acc_pltf',
                'verbose_name_plural': 'log_acc_pltfs',
            },
        ),
        migrations.CreateModel(
            name='log_acc_mod',
            fields=[
                ('id_log_acces', models.AutoField(primary_key=True, serialize=False)),
                ('fch_ini', models.DateField(verbose_name='fecha de inicio')),
                ('fch_fin', models.DateField(verbose_name='fecha de fin')),
                ('id_mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.mod')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'log_acc_mod',
                'verbose_name_plural': 'log_acc_mods',
            },
        ),
        migrations.CreateModel(
            name='ext_mod',
            fields=[
                ('id_mod_ext', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_ext', models.CharField(max_length=40, verbose_name='Título de la aplicacion: ')),
                ('mod_prin_ext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.mod')),
            ],
            options={
                'verbose_name': 'ext_mod',
                'verbose_name_plural': 'ext_mods',
            },
        ),
        migrations.CreateModel(
            name='ext_app',
            fields=[
                ('id_app_ext', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_app_ext', models.CharField(max_length=40, verbose_name='Título de la aplicacion: ')),
                ('mod_prin_app_ext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.app_mod')),
            ],
            options={
                'verbose_name': 'ext_app',
                'verbose_name_plural': 'ext_apps',
            },
        ),
        migrations.AddField(
            model_name='app_mod',
            name='mod_prin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.mod'),
        ),
    ]
