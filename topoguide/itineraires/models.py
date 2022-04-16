from django.db import models

class Itineraire(models.Model):
    title = models.CharField(max_length=200)
    departure = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    altitude_dep = models.IntegerField(default=0)
    altitude_min = models.IntegerField(default = 0)
    altitude_max = models.IntegerField(default = 0)
    height_dif_pos = models.IntegerField(default=0)
    height_dif_neg = models.IntegerField(default=0)
    duration = models.IntegerField(default = 0)
    difficulty = models.IntegerField(default=1)

    
