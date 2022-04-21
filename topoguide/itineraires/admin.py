from django.contrib import admin

from .models import Itineraire, Sortie

# Permet d'autoriser l'admin à modifier les itinéraires et les sorties
admin.site.register(Itineraire)
admin.site.register(Sortie)
