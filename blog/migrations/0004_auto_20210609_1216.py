# Generated by Django 3.2.3 on 2021-06-09 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210609_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imagen1',
            new_name='imagen',
        ),
        migrations.AlterField(
            model_name='imagen',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagen_post', to='blog.post'),
        ),
    ]