# Generated by Django 4.0.3 on 2022-04-02 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Departamento',
            new_name='Unidade',
        ),
        migrations.RenameField(
            model_name='materia',
            old_name='departamento',
            new_name='unidade',
        ),
    ]
