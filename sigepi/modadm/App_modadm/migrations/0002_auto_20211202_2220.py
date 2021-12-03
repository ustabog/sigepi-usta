# Generated by Django 3.2.8 on 2021-12-03 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_modadm', '0001_initial'),
    ]

    operations = [
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
            model_name='rol',
            name='id_sis',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='App_modadm.listado_aplicativo'),
            preserve_default=False,
        ),
    ]
