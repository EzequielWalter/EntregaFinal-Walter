# Generated by Django 4.1.1 on 2022-10-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_familiar_delete_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]