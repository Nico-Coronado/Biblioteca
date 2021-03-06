# Generated by Django 3.2.5 on 2021-11-25 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prestamo', '0001_initial'),
        ('libro', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='lector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libro_prestamo', to='libro.libro'),
        ),
    ]
