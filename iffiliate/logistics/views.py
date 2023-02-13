from django.shortcuts import render
from .models import LogisticCompany, LogisticPrice, Dispatch, Rider
from .serializers import LogisticCompanySerializer, LogisticPriceSerializer, RidersSerializer, DispatchSerializer
# Create your views here.


class AllInfo:

    def Companies(self):
        companies = LogisticCompany.objects.all()
        companies = LogisticCompanySerializer(data=companies, many=True)
        serialized_data = companies.data
        return serialized_data

    def Companies_price(self):
        companies_price = LogisticPrice.objects.all()
        companies_price = LogisticPriceSerializer(data=companies_price, many=True)
        serialized_data = companies_price.data
        return serialized_data

    def Rider(self):
        riders = Rider.objects.all()
        riders = RidersSerializer(data=riders, many=True)
        serialized_data = riders.data
        return serialized_data

    def Dispatch(self):
        dispatch = Dispatch.objects.all()
        dispatch = DispatchSerializer(data=dispatch, many=True)
        serialized_data = dispatch.data
        return serialized_data


class SingleInfo:
    def __init__(self, company_name):
        self.name = company_name

        if company_name is None:
            raise NameError('company\'s name cannot be None ')
        try:
            company = LogisticCompany.objects.get(name=company_name)
        except LogisticCompany.DoesNotExist:
            raise LookupError('company\'s name doesnot exist')
        self.company = company

    def Company(self):
        company = LogisticCompanySerializer(data=self.company)
        serialized_data = company.data
    def Companies_price(self):
        companies_price = LogisticPrice.objects.get(company=self.company)
        companies_price = LogisticPriceSerializer(data=companies_price)
        serialized_data = companies_price.data
        return serialized_data
