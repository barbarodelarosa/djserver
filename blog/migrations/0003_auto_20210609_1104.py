# Generated by Django 3.2.3 on 2021-06-09 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_imagen_creado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categoria',
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ManyToManyField(related_name='categoria_post', to='blog.CategoriaPost'),
        ),
    ]
