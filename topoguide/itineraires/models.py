from django.contrib.auth.models import User
from django.db import models


class Itineraire(models.Model):
    """
    Une classe itinéraire qui comprend différentes informations

    Args:
        models (): Model

    """
    title = models.CharField(max_length=200)
    departure = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    altitude_dep = models.IntegerField(default=0)
    altitude_min = models.IntegerField(default = 0)
    altitude_max = models.IntegerField(default = 0)
    height_dif_pos = models.IntegerField(default=0)
    height_dif_neg = models.IntegerField(default=0)
    # une durée au format 00:00:00 (h:min:sec)
    duration = models.DurationField()
    difficulty = models.CharField(choices = [('1', '1'),('2', '2'),('3','3'),('4', '4'),('5','5')], max_length=3)
        
    def __str__(self):
        return self.title

class Sortie(models.Model):
    """
    Une classe sortie avec les informations associées

    Args:
        models (): Model

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itineraire = models.ForeignKey(Itineraire, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()
    people = models.IntegerField(default = 1)
    group_exp = models.CharField(choices= [('tous débutants','tous débutants'), ('tous expérimentés','tous expérimentés'), ('mixte','mixte' )], max_length=100 )
    weather = models.CharField(choices = [('bonne','bonne'), ('moyenne','moyenne'), ('mauvaise','mauvaise')], max_length=100)
    difficulty = models.CharField(choices = [('1', '1'),('2', '2'),('3','3'),('4', '4'),('5','5')], max_length=3)
    
    def __str__(self):
        return self.itineraire.title + " by " + self.user.username  