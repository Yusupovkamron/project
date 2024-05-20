from rest_framework import serializers
from .models import Sweets, Discounts, Masters, Clients, Locations


class SweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweets
        fields = "__all__"


class DiscountsSerializer(serializers.ModelSerializer):
    sweets = SweetsSerializer()

    class Meta:
        model = Discounts
        fields = "__all__"


class MastersSerializer(serializers.ModelSerializer):
    discounts = DiscountsSerializer(read_only=True)

    class Meta:
        model = Masters
        fields = "__all__"


class ClientsSerializer(serializers.ModelSerializer):
    masters = MastersSerializer(read_only=True)

    class Meta:
        model = Clients
        fields = "__all__"


class LocationsSerializer(serializers.ModelSerializer):
    clients = ClientsSerializer(read_only=True)

    class Meta:
        model = Locations
        fields = "__all__"

