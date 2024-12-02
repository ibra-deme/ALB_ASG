from django.db import models

class Trajet(models.Model):
    depart=models.CharField(max_length=200,null=True)
    arrive=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.depart
# Create your models here.
