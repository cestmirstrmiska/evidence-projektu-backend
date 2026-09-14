from rest_framework import serializers
from .models import Osoba, Projekt


class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = '__all__'


class ProjektSerializer(serializers.ModelSerializer):
    # Detailní výpis členů (pouze pro čtení)
    clenove_detail = OsobaSerializer(many=True, read_only=True, source='clenove')

    # OPRAVA: Definujeme pole 'clenove' pro zápis s parametrem required=False
    # To umožní předat prázdný seznam [] a založit projekt bez lidí.
    clenove = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Osoba.objects.all(),
        required=False  # <-- TENTO PARAMETR ZDE CHYBĚL!
    )

    class Meta:
        model = Projekt
        fields = ['id', 'nazev', 'popis', 'start_date', 'end_date', 'stav', 'clenove', 'clenove_detail']

    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')

        if self.instance:
            if start_date is None:
                start_date = self.instance.start_date
            if end_date is None:
                end_date = self.instance.end_date

        if start_date and end_date:
            if end_date < start_date:
                raise serializers.ValidationError({
                    "end_date": "Datum ukončení projektu nemůže nastat dříve než datum jeho zahájení."
                })

        return attrs
