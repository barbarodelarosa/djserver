# Generated by Django 3.2.5 on 2021-08-02 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imc', '0003_rename_result_imctest_imc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imc',
            old_name='result',
            new_name='imc',
        ),
        migrations.AlterField(
            model_name='imc',
            name='calification',
            field=models.CharField(max_length=50),
        ),
    ]