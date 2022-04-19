
from django.forms import ModelForm

from itineraires.models import Sortie

class SortieForm(ModelForm):
    class Meta:
        model = Sortie
        fields = ['itineraire', 'user', 'date', 'duration', 'people', 'group_exp', 'weather', 'difficulty']