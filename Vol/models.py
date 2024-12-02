from django.db import models
from Trajet.models import Trajet
from Compagnie.models import Compagnie
class Vol(models.Model):
    prix=models.FloatField(null=True)
    date=models.CharField(max_length=200,null=True)
    heure=models.CharField(max_length=200,null=True)
    trajet=models.ForeignKey(Trajet,null=True,on_delete=models.CASCADE)
    compagnie=models.ManyToManyField(Compagnie)

    def __str__(self):
        return self.heure
# Create your models here.
