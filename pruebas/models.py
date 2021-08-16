from django.db import models
from usuario.models import OwnerModel
from django.utils import timezone
# Create your models here.

class TestCategory(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class EmotionState(OwnerModel):
    emotion_name    = models.CharField(max_length=15, blank=True, null=True)
    emotion_value   = models.IntegerField(default=0)
    created_at      = models.DateTimeField(default=timezone.now)
    icon            = models.CharField(max_length=100)
    public          = models.BooleanField(default=True)

    def __str__(self):
        return self.emotion_name