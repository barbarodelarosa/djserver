from rest_framework import serializers

from usuario.models import User


class UsuarioSerializers(serializers.ModelSerializer):
    email    = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()
    avatar   = serializers.ImageField(required = False)
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

        ]

class OwnerSerializers(serializers.ModelSerializer):

    aprobado = serializers.HiddenField(default=False)
    class Meta:
        model=User
        fields=["id","email","avatar","username","first_name","last_name","aprobado","movil"]




