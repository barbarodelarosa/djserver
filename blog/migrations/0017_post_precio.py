# Generated by Django 3.2.5 on 2021-08-15 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='precio',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
