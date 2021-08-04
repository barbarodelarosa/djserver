from django.db import models
from usuario.models import OwnerModel
from django.utils import timezone
from imc.utils import calcular_imc, calificacion_imc
from pruebas.models import TestCategory
class IMC(OwnerModel):
    category    = models.ForeignKey(TestCategory, on_delete=models.CASCADE, null=True)
    talla       = models.FloatField(blank=True, null=True)
    peso        = models.FloatField(blank=True, null=True)
    imc         = models.FloatField(blank=True, null=True)
    created     = models.DateTimeField(default=timezone.now)
    calification= models.CharField(max_length=50, blank=True, null=True)
    message     = models.TextField(max_length=500, blank=True, null=True)
    private     = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s" %(self.category, self.owner)

    def save(self, *args, **kwargs):
        self.imc = calcular_imc(self.peso, self.talla)
        self.calification = calificacion_imc(self.imc)
        super().save(*args, **kwargs)

class IMCTest(models.Model):
    talla       = models.FloatField(blank=True, null=True)
    peso        = models.FloatField(blank=True, null=True)
    imc         = models.FloatField(blank=True, null=True)
    created     = models.DateTimeField(default=timezone.now)
    calification= models.CharField(max_length=50, blank=True, null=True)
    message     = models.TextField(max_length=500, blank=True, null=True)
    private     = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.imc = calcular_imc(self.peso, self.talla)
        self.calification = calificacion_imc(self.imc)
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.created
# Create your models here.
