# Generated by Django 3.2.5 on 2021-08-02 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMCTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.FloatField(blank=True, null=True)),
                ('peso', models.FloatField(blank=True, null=True)),
                ('result', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('calification', models.FloatField(blank=True, null=True)),
                ('message', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
