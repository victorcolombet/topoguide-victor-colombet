
from django.forms import ModelForm

from itineraires.models import Sortie

class SortieForm(ModelForm):
    """
    Un forumaire pour ajouter une sortie à la base de donnée

    Args:
        ModelForm :  un ModelForm 
    """
    class Meta:
        model = Sortie
        fields = ['itineraire', 'date', 'duration', 'people', 'group_exp', 'weather', 'difficulty']

class ModifSortieForm(ModelForm):
    """
    Un formulaire pour modifier une sortie déjà présente

    Args:
        ModelForm (): un ModelForm
    """
    class Meta:
        model = Sortie
        fields = ['itineraire', 'date', 'duration', 'people', 'group_exp', 'weather', 'difficulty']