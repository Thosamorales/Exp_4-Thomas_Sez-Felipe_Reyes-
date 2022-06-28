from django.urls import path
from .views import lista_colaboradores

urlpatterns=[ 
    path('lista_colaboradores', lista_colaboradores, name="lista_colaboradores"),
]