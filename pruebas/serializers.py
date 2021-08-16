from rest_framework import serializers

from pruebas.models import EmotionState


class EmotionStateSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    public = serializers.HiddenField(default=True)
    class Meta:
        model=EmotionState
        fields='__all__'