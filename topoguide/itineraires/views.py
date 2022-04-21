from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from itineraires.models import Itineraire, Sortie
from itineraires.forms import *


@login_required()
def itineraires(request):
    """
    Une vue itineraires qui comprend la liste des itinéraires de la base données

    Args:
        request (): requete utilisateur

    Returns:
        la page html associée à la vue 
    """
    itineraires_list = Itineraire.objects.order_by('-title')
    context = {'itineraires_list': itineraires_list}
    return render(request, 'itineraires/itineraires.html', context)


@login_required()
def sorties(request, itineraire_id):
    """
    Une vue sorties qui comprend la liste des sorties pour un itinéraire donné

    Args:
        request (): requete utilisateur
        itineraire_id (): l'itineraire dont on veut voir les sorties

    Returns:
        la page html associée à la vue
    """
    itineraire = get_object_or_404(Itineraire, pk=itineraire_id)
    return render(request,'itineraires/sorties.html', {'itineraire' : itineraire})


@login_required()
def sortie(request, sortie_id):
    """
    Une vue sortie qui comprend les informations relatives à une sortie, telle qu'à pu le rentrer un utilisateur

    Args:
        request (): requete utilisateur
        sortie_id (): la sortie dont on veut voir les informations

    Returns:
        la page html associée à la vue
    """
    sortie = get_object_or_404(Sortie, pk=sortie_id)
    return render(request,'itineraires/sortie.html', {'sortie' : sortie} )


@login_required()
def nouvelle_sortie(request):
    """
    Une vue nouvelle_sortie qui permet de créer une nouvelle sortie dans la base de données

    Args:
        request (): requete utilisateur

    Returns:
        Le formulaire de saisie dans le cas d'une requete get, ou bien la création d'une nouvelle sortie et la redirection vers la page itinéraires une fois le formulaire complété
    """
    if request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            #on fait en sorte que le user associé à la sortie crée soit le user connecté à la session
            nouvelle_sortie = form.save(commit=False)
            nouvelle_sortie.user = request.user
            nouvelle_sortie.save()
            # on redirige vers la page itineraire
            return redirect('/itineraires/')
    elif request.method == 'GET':
        # on crée puis affiche le formulaire à compléter
        form = SortieForm()
    return render(request, 'itineraires/nouvelle_sortie.html', {'form' : form})

@login_required()
def modif_sortie(request, sortie_id):
    """
    Une vue modif_sortie qui permet de modifier une sortie déjà présente dans la base de données

    Args:
        request (): requete utilisateur
        sortie_id (): l'identifiant de la sortie que l'on veut modifier

    Returns:
        la sortie est modifiée et une redirection vers la page itineraire
    """
    sortie = get_object_or_404(Sortie, pk = sortie_id)
    if request.method == 'GET':
        # on crée puis affiche le forulaire à compléter, avec une instance de sortie
        form = ModifSortieForm(instance=sortie)
    elif request.method == 'POST':
        form = ModifSortieForm(request.POST, instance=sortie)
        if form.is_valid() and sortie.user == request.user:
            # on vérifie que le user connecté soit le même que celui qui a crée la sortie
            modif_sortie = form.save(commit=False)
            modif_sortie.user = request.user
            modif_sortie.save()
            # redirection vers la page itineraires
            return redirect('/itineraires/')
    return render(request, 'itineraires/modif_sortie.html', {'form' : form})
            