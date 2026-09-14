from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Osoba, Projekt
from .serializers import OsobaSerializer, ProjektSerializer

class OsobaViewSet(viewsets.ModelViewSet):
    serializer_class = OsobaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['jmeno', 'prijmeni', 'pozice', 'email']

    def get_queryset(self):
        queryset = Osoba.objects.all().order_by('prijmeni', 'jmeno')
        # Zachycení parametru ?pozice= z URL adresy
        vybrana_pozice = self.request.query_params.get('pozice', None)
        if vybrana_pozice:
            queryset = queryset.filter(pozice=vybrana_pozice)
        return queryset


class ProjektViewSet(viewsets.ModelViewSet):
    serializer_class = ProjektSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nazev', 'popis', 'stav']

    def get_queryset(self):
        queryset = Projekt.objects.all().prefetch_related('clenove').order_by('-start_date')
        # Zachycení parametru ?stav= z URL adresy
        vybrany_stav = self.request.query_params.get('stav', None)
        if vybrany_stav:
            queryset = queryset.filter(stav=vybrany_stav)
        return queryset
