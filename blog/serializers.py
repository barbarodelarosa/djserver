from rest_framework import serializers

from blog.models import Post, Comentario, Imagen, CategoriaPost
from usuario.models import User
from usuario.serializers import OwnerSerializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from datetime import timezone

from drf_extra_fields.fields import Base64ImageField
class ComentarioSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=Comentario
        fields='__all__'



class CategoriaPostSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=CategoriaPost
        fields='__all__'



class PostSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=Post
        fields='__all__'


class ImagenSerializers(serializers.ModelSerializer):

    imagen=Base64ImageField(
        max_length=None, use_url=True, required=False
    )

    class Meta:
        model=Imagen
        fields='__all__'

    # def create(self, validated_data):
    #     return Imagen.objects.create(**validated_data)




class PostNestedSerializer(WritableNestedModelSerializer):
    owner = OwnerSerializers(allow_null=True)
    aprobado = serializers.HiddenField(default=False)
    categoria = CategoriaPostSerializers(many=True)
    post_comentario = ComentarioSerializers(many=True)
    post_imagen = ImagenSerializers(many=True)

    class Meta:
        model=Post
        fields='__all__'

class PostUserNestedSerializer(WritableNestedModelSerializer):
    owner = OwnerSerializers(allow_null=True)
    aprobado = serializers.HiddenField(default=False)
    categoria = CategoriaPostSerializers(many=True)
    post_comentario = ComentarioSerializers(many=True)

    class Meta:
        model=Post
        fields='__all__'

class CategoriaPostNestedSerializer(WritableNestedModelSerializer):

    categoria_post = PostUserNestedSerializer(many=True)

    class Meta:
        model=CategoriaPost
        fields='__all__'





class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):

        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr
        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension



class LikePostSerializers(serializers.ModelSerializer):

    class Meta:
        model=Post
        fields=['id','likes']

class ReportPostSerializers(serializers.ModelSerializer):

    class Meta:
        model=Post
        fields=['id','reports']