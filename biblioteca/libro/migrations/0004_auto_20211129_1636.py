# Generated by Django 3.2.5 on 2021-11-29 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_auto_20211126_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Authors',
            new_name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='adfs', max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Categoria'),
        ),
    ]
