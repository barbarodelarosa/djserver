# Generated by Django 3.2.3 on 2021-06-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
    ]