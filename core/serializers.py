from rest_framework import serializers
from .models import Osoba, Projekt


class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = '__all__'


class ProjektSerializer(serializers.ModelSerializer):
    # Přepíšeme pole 'clenove', aby serializer při GET dotazu vracel detailní info o lidech,
    # ale při zápisu (POST/PUT/PATCH) přijímal pouze seznam jejich ID.
    clenove_detail = OsobaSerializer(many=True, read_only=True, source='clenove')

    class Meta:
        model = Projekt
        fields = ['id', 'nazev', 'popis', 'start_date', 'end_date', 'stav', 'clenove', 'clenove_detail']

    # POKROČILÁ VALIDACE PRO REST API (Bod 2 zadání)
    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')

        # Pokud provádíme PATCH (částečnou úpravu), musíme si data dohledat ze stávajícího objektu
        if self.instance:
            if start_date is None:
                start_date = self.instance.start_date
            if end_date is None:
                end_date = self.instance.end_date

        # 1. Validace logického rozsahu datumů
        if start_date and end_date:
            if end_date < start_date:
                raise serializers.ValidationError({
                    "end_date": "Datum ukončení projektu nemůže nastat dříve než datum jeho zahájení."
                })

        return attrs
