# Generated by Django 4.1.4 on 2022-12-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundial_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='anio_creacion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='dorsal',
            field=models.IntegerField(),
        ),
    ]
