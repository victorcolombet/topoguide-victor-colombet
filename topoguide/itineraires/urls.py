from django.urls import path
from . import views

app_name = 'itineraires'
urlpatterns = [
    path('itineraires/', views.itineraires, name = 'itineraires'),
    path('sorties/<str:itineraire_id>/', views.sorties, name='sortie')
]