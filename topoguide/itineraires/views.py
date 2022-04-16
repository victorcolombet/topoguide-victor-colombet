from django.shortcuts import get_object_or_404, render

from itineraires.models import Itineraire
from itineraires.models import Sortie

# Create your views here.

def itineraires(request):
    itineraires_list = Itineraire.objects.order_by('-title')
    context = {'itineraires_list': itineraires_list}
    return render(request, 'itineraires/itineraires.html', context)

def sorties(request, itineraire_id):
    itineraire = get_object_or_404(Itineraire, pk=itineraire_id)
    return render(request,'itineraires/sorties.html', {'itineraire' : itineraire})
    