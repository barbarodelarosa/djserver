# Generated by Django 3.2.3 on 2021-06-20 04:30

from django.db import migrations, models
import usuario.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=usuario.models.path_to_avatar),
        ),
    ]
