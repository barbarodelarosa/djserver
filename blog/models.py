import datetime
from django.utils import timezone
from django.db import models
from django.contrib.contenttypes.models import ContentType
from usuario.models import User, OwnerModel
# Create your models here.
import os, uuid
from djserver.utils import ResizeImageMixin


def nombreArchivo(instance, filename):
    nombre = filename.split('.')
    extension = nombre[-1]
    print(uuid.uuid4())
    idfoto = str(uuid.uuid4())
    nombrefinal = os.path.join(idfoto + '.' + extension)
    print(nombrefinal)
    return '/'.join(['imagenes/blog', str(instance.nameclass), nombrefinal])

class CategoriaPost(models.Model, ResizeImageMixin):
    nameclass = 'CategoriaPost'
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to=nombreArchivo, blank=True, null=True)
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.imagen:
                self.resize(self.imagen, (400, 400))
            else:
                pass
        super().save(*args, **kwargs)



class Post(OwnerModel, ResizeImageMixin):
    nameclass = 'Post'

    categoria=models.ManyToManyField(CategoriaPost, related_name='categoria_post', blank=True)
    titulo=models.CharField(max_length=140, blank=True, null=True)
    mensaje=models.TextField(max_length=1500, blank=True, null=True)
    coordenadas=models.CharField(max_length=140, blank=True, null=True)
    imagen=models.ImageField(upload_to=nombreArchivo, blank=True, null=True)
    creado=models.DateTimeField(default=timezone.now, blank=True, null=True)
    actualizado=models.DateTimeField('Fecha de actualizacion', blank=True, null=True, auto_now=True)
    votos=models.IntegerField(default=0, blank=True, null=True)
    compartido = models.IntegerField(default=0, blank=True, null=True)
    aprobado = models.BooleanField(default=False, blank=True, null=True)
    vistas = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')


    def total_likes(self):
        return self.likes.count()


    def aprovado(self):
        self.aprobado = True
        self.save()

    def __str__(self):
        return self.titulo

    def fecha_publicado(self):
        return self.creado >= timezone.now() - datetime.timedelta(days=1)

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.imagen:
                self.resize(self.imagen, (400, 400))
            else:
                pass
        super().save(*args, **kwargs)


class Comentario(OwnerModel):
    nameclass = 'Comentario'
    texto = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comentario')
    votos = models.IntegerField(default=0)
    creado = models.DateTimeField(default=timezone.now)
    compartido = models.IntegerField(default=0)
    aprobado = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, blank=True, related_name='likes_comentario')

    def total_likes(self):
        return self.likes.count()


    def aprovado(self):
        self.aprobado = True
        self.save()

    def __str__(self):
        return self.texto


class Imagen(models.Model, ResizeImageMixin):
    nameclass = 'ImagenPost'
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_imagen', blank=True, null=True)
    enlace = models.URLField(blank=True, null=True, max_length=100)
    imagen = models.ImageField(upload_to=nombreArchivo, blank=True, null=True)
    texto = models.CharField(blank=True, null=True, max_length=100)
    creado = models.DateTimeField(default=timezone.now, blank=True, null=True)



    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.imagen:
                self.resize(self.imagen, (400, 400))
            else:
                pass
        super().save(*args, **kwargs)





