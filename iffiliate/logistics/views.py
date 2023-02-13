from django.shortcuts import render
from .models import LogisticCompany, LogisticPrice, Dispatch
from .serializers import LogisticCompanySerializer, LogisticPriceSerializer
# Create your views here.


class AllLogisticsInfo:

    def Companies(self):
        companies = LogisticCompany.objects.all()
        companies = LogisticCompanySerializer(data=companies, many=True)
        serialized_data = companies.data
        return serialized_data


