# Generated by Django 3.2.5 on 2021-08-03 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pruebas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMCTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.FloatField(blank=True, null=True)),
                ('peso', models.FloatField(blank=True, null=True)),
                ('imc', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('calification', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IMC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.FloatField(blank=True, null=True)),
                ('peso', models.FloatField(blank=True, null=True)),
                ('imc', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('calification', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(blank=True, max_length=500, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pruebas.testcategory')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
