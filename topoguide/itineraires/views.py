from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from itineraires.models import Itineraire
from itineraires.models import Sortie
from itineraires.forms import *

# Create your views here.

@login_required()
def itineraires(request):
    itineraires_list = Itineraire.objects.order_by('-title')
    context = {'itineraires_list': itineraires_list}
    return render(request, 'itineraires/itineraires.html', context)

@login_required()
def sorties(request, itineraire_id):
    itineraire = get_object_or_404(Itineraire, pk=itineraire_id)
    return render(request,'itineraires/sorties.html', {'itineraire' : itineraire})

@login_required()
def sortie(request, sortie_id):
    sortie = get_object_or_404(Sortie, pk=sortie_id)
    return render(request,'itineraires/sortie.html', {'sortie' : sortie} )

@login_required()
def nouvelle_sortie(request):
    if request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            nouvelle_sortie = form.save(commit=False)
            nouvelle_sortie.user = request.user
            nouvelle_sortie.save()
            return redirect('/itineraires/')
    elif request.method == 'GET':
        form = SortieForm()
    return render(request, 'itineraires/nouvelle_sortie.html', {'form' : form})

@login_required()
def modif_sortie(request, sortie_id):
    sortie = get_object_or_404(Sortie, pk = sortie_id)
    if request.method == 'GET':
        form = ModifSortieForm(instance=sortie)
    elif request.method == 'POST':
        form = ModifSortieForm(request.POST, instance=sortie)
        if form.is_valid() and sortie.user == request.user:
            modif_sortie = form.save(commit=False)
            modif_sortie.user = request.user
            modif_sortie.save()
            return redirect('/itineraires/')
    return render(request, 'itineraires/modif_sortie.html', {'form' : form})
            