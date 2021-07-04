# Generated by Django 3.2.3 on 2021-06-24 22:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='aprobado',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.ManyToManyField(blank=True, null=True, related_name='categoria_post', to='blog.CategoriaPost'),
        ),
        migrations.AlterField(
            model_name='post',
            name='compartido',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='creado',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='votos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
