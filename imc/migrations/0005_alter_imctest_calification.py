# Generated by Django 3.2.5 on 2021-08-02 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imc', '0004_auto_20210802_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imctest',
            name='calification',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
