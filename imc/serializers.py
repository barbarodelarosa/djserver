from rest_framework import serializers

from imc.models import IMC
from usuario.models import User
from usuario.serializers import OwnerSerializers
from datetime import timezone

from drf_extra_fields.fields import Base64ImageField
class IMCSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model=IMC
        fields='__all__'


