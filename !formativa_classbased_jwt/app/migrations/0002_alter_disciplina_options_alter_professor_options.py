# Generated by Django 5.2 on 2025-05-08 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disciplina',
            options={'verbose_name_plural': 'Disciplina'},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name_plural': 'Professor'},
        ),
    ]
