# Generated by Django 4.1.2 on 2022-11-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avanzado', '0004_rename_edad_mascota_edad_media_de_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
