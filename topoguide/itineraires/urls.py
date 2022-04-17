from django.urls import path
from . import views

app_name = 'itineraires'
urlpatterns = [
    path('itineraires/', views.itineraires, name = 'itineraires'),
    path('sorties/<str:itineraire_id>/', views.sorties, name='sorties'),
    path('sortie/<str:sortie_id>/', views.sortie, name='sortie'),
    path('nouvelle_sortie/', views.views.nouvelle_sortie, name='nouvelle_sortie')
]