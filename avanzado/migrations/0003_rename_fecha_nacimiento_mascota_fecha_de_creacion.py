# Generated by Django 4.1.2 on 2022-11-10 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avanzado', '0002_mascota_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='fecha_nacimiento',
            new_name='fecha_de_creacion',
        ),
    ]
