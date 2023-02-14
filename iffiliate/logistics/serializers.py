from rest_framework import serializers
from .models import LogisticCompany, LogisticPrice, Location, Rider


class LogisticCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogisticCompany
        fields = ['name']

class LogisticPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogisticPrice
        fields = ['company_name', 'value_per_goods', 'price_per_weight']


class RidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ['company_name', 'name', 'phone_number']

class DispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['company_name', 'country', 'state', 'city', 'price']