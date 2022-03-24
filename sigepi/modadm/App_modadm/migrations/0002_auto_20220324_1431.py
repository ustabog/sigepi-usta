# Generated by Django 3.2.8 on 2022-03-24 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_modadm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='id_ext_app',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App_modadm.ext_app'),
        ),
        migrations.AddField(
            model_name='rol',
            name='id_ext_mod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App_modadm.ext_mod'),
        ),
        migrations.AddField(
            model_name='rol',
            name='id_sis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App_modadm.listado_aplicativo'),
        ),
    ]