# Generated by Django 3.2.3 on 2021-06-13 06:01

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import usuario.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20210613_0147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='user',
            name='actualizado',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='amigos',
            field=models.ManyToManyField(blank=True, related_name='_usuario_user_amigos_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=usuario.models.path_to_avatar),
        ),
        migrations.AddField(
            model_name='user',
            name='calle',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='compartido',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='coordenadas',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='correo',
            field=models.EmailField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='creado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='user',
            name='edad',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.URLField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='genero',
            field=models.CharField(choices=[('', ''), ('M', 'Masculino'), ('F', 'Femenino')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='user',
            name='localidad',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='movil',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='municipio',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='pais',
            field=models.CharField(default='Cuba', max_length=25),
        ),
        migrations.AddField(
            model_name='user',
            name='provincia',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='seguidores',
            field=models.ManyToManyField(blank=True, related_name='_usuario_user_seguidores_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='sitio_web',
            field=models.URLField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='telegram',
            field=models.URLField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='tipo_usuario',
            field=models.IntegerField(blank=True, choices=[(1, 'ADMIN'), (2, 'EMPRENDEDOR'), (3, 'USER')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='whatsapp',
            field=models.URLField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
