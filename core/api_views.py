from rest_framework import viewsets
from rest_framework.filters import SearchFilter  # PŘIDAT TENTO IMPORT
from .models import Osoba, Projekt
from .serializers import OsobaSerializer, ProjektSerializer


class OsobaViewSet(viewsets.ModelViewSet):
    queryset = Osoba.objects.all().order_by('prijmeni', 'jmeno')
    serializer_class = OsobaSerializer

    # Aktivace vyhledávání na pozadí backendu
    filter_backends = [SearchFilter]
    search_fields = ['jmeno', 'prijmeni', 'pozice', 'email']  # Sloupce pro fulltext


class ProjektViewSet(viewsets.ModelViewSet):
    queryset = Projekt.objects.all().prefetch_related('clenove').order_by('-start_date')
    serializer_class = ProjektSerializer

    # Aktivace vyhledávání na pozadí backendu
    filter_backends = [SearchFilter]
    search_fields = ['nazev', 'popis', 'stav']  # Sloupce pro fulltext
