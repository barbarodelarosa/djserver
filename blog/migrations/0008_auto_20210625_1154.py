# Generated by Django 3.2.3 on 2021-06-25 15:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210624_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='creado',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_imagen', to='blog.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.ManyToManyField(blank=True, related_name='categoria_post', to='blog.CategoriaPost'),
        ),
    ]