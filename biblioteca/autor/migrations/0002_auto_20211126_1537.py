# Generated by Django 3.2.5 on 2021-11-26 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='nacionalidad',
        ),
    ]