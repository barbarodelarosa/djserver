from django.db import models
import uuid, os
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.contenttypes.models import ContentType
from djserver.utils import ResizeImageMixin

class OwnerModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract=True


def path_to_avatar(instance, filename):
    nombre = filename.split('.')
    extension = nombre[-1]
    print(uuid.uuid4())
    idfoto = str(uuid.uuid4())
    nombrefinal = os.path.join(idfoto + '.' + extension)
    print(nombrefinal)
    return '/'.join(['imagenes', str(instance.id),'avatars', nombrefinal])

USER_TYPE = (
    (1, 'ADMIN'),
    (2, 'EMPRENDEDOR'),
    (3, 'USER'),

)
GENERO = [
    ('', ""),
    ('M', "Masculino"),
    ('F', "Femenino")
]


class User(AbstractUser, ResizeImageMixin):
    email = models.EmailField(max_length=150, unique=True)
    uid = models.CharField(max_length=52, blank=True, null=True)
    tipo_usuario = models.IntegerField(choices=USER_TYPE, default=1, blank=True, null=True)
    amigos = models.ManyToManyField("self", related_name='amigos', blank=True)
    avatar = models.ImageField(upload_to=path_to_avatar, null=True, blank=True)
    birthday = models.DateField(auto_now_add=True, null=True, blank=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    genero = models.CharField(max_length=10, choices=GENERO, default='')
    seguidores=models.ManyToManyField("self", related_name='usuario_seguidores', blank=True, symmetrical=False)
    compartido = models.IntegerField(default=0)
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(blank=True, null=True, auto_now=True)
    telefono = models.CharField(max_length=15, blank=True, null=True, unique=True)
    movil = models.CharField(max_length=15, blank=True, null=True, unique=True)
    correo = models.EmailField(blank=True, null=True, max_length=30, unique=True)
    sitio_web = models.URLField(blank=True, null=True, max_length=30, unique=True)
    facebook = models.URLField(blank=True, null=True, max_length=30, unique=True)
    instagram = models.URLField(blank=True, null=True, max_length=30, unique=True)
    whatsapp = models.URLField(blank=True, null=True, max_length=30, unique=True)
    telegram = models.URLField(blank=True, null=True, max_length=30, unique=True)
    pais = models.CharField(default='Cuba', max_length=25)
    provincia = models.CharField(blank=True, null=True, max_length=25)
    municipio = models.CharField(blank=True, null=True, max_length=25)
    localidad = models.CharField(blank=True, null=True, max_length=25)
    calle = models.CharField(blank=True, null=True, max_length=25)
    coordenadas = models.CharField(max_length=60, blank=True, null=True)
    presentation = models.TextField(max_length=300, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def total_amigos(self):
        return self.amigos.count()

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.avatar:
                self.resize(self.avatar, (400, 400))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email





class Code(OwnerModel):
    code=models.CharField(max_length=15)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code