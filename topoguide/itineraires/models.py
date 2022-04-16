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
    duration = models.DurationField()
    difficulty = models.IntegerField(choices = [1,2,3,4,5])

class Sortie(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE)
    itineraire = models.ForeignKey(Itineraire, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()
    people = models.IntegerField(default = 1)
    group_exp = models.CharField(choices= ['tous débutants', 'tous expérimentés', 'mixte'] )
    weather = models.CharField(choices = ['bonne', 'moyenne', 'mauvaise'])
    difficulty = models.IntegerField(choices = [1,2,3,4,5])