from rest_framework import viewsets
from .models import Osoba, Projekt
from .serializers import OsobaSerializer, ProjektSerializer

class OsobaViewSet(viewsets.ModelViewSet):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer

class ProjektViewSet(viewsets.ModelViewSet):
    queryset = Projekt.objects.all()
    serializer_class = ProjektSerializer
