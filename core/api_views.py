from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action          # PŘIDAT TENTO IMPORT
from rest_framework.response import Response          # PŘIDAT TENTO IMPORT
from .models import Osoba, Projekt
from .serializers import OsobaSerializer, ProjektSerializer

class OsobaViewSet(viewsets.ModelViewSet):
    serializer_class = OsobaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['jmeno', 'prijmeni', 'pozice', 'email']

    def get_queryset(self):
        queryset = Osoba.objects.all().order_by('prijmeni', 'jmeno')
        vybrana_pozice = self.request.query_params.get('pozice', None)
        if vybrana_pozice:
            queryset = queryset.filter(pozice=vybrana_pozice)
        return queryset

    # NOVÉ: Dynamický číselník unikátních pozic z databáze (přístupný na /api/osoby/pozice/)
    @action(detail=False, methods=['get'])
    def pozice(self, request):
        # Vytáhne z DB unikátní pozice, které nejsou prázdné
        unikatni_pozice = Osoba.objects.values_list('pozice', flat=True).distinct().order_by('pozice')
        return Response(list(unikatni_pozice))


class ProjektViewSet(viewsets.ModelViewSet):
    # ... (Tato třída zůstává beze změny z minula) ...
    serializer_class = ProjektSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nazev', 'popis', 'stav']

    def get_queryset(self):
        queryset = Projekt.objects.all().prefetch_related('clenove').order_by('-start_date')
        vybrany_stav = self.request.query_params.get('stav', None)
        if vybrany_stav:
            queryset = queryset.filter(stav=vybrany_stav)
        return queryset
