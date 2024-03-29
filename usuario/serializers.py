from rest_framework import serializers

from usuario.models import User
from drf_extra_fields.fields import Base64ImageField

class UsuarioSerializers(serializers.ModelSerializer):
    email    = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()
    # avatar   = serializers.ImageField(allow_null=True)
    avatar   = Base64ImageField(
        max_length=None, use_url=True, required=False, allow_null=True
    )

    # avatar   = serializers.ImageField(required = False)
    class Meta:
        model=User
        fields=[
            'id',
            'username',
            'first_name',
            'last_name',
            'date_joined',
            'email',
            'uid',
            'amigos',
            'avatar',
            'movil',
            'presentation',
            'seguidores',
            'usuario_seguidores',
            'birthday',
            'age',
            'height',
            'weight',
            'post_set',

        ]

class OwnerSerializers(serializers.ModelSerializer):

    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=User
        fields=["id","email","avatar","username","first_name","last_name","aprobado","movil"]



class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):

        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            decoded_file = ''
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