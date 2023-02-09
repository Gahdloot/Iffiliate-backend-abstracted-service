from rest_framework import serializers
from .models import LogisticCompany, LogisticPrice, Dispatch, Rider


class LogisticCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogisticCompany
        fields = ['name']

