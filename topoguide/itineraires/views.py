from django.shortcuts import render

from topoguide.itineraires.models import Itineraire

# Create your views here.

def itineraires(request):
    itineraires_list = Itineraire.objects.order_by('-title')
    context = {'itineraires_list': itineraires_list}
    return render(request, 'itineraires/itineraires.html', context)