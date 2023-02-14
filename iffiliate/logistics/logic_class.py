from .models import LogisticCompany, LogisticPrice, Location, Rider
from .serializers import LogisticCompanySerializer, LogisticPriceSerializer, RidersSerializer, LocationSerializer
# Create your views here.


class AllInfo:

    def companies(self):
        companies = LogisticCompany.objects.all()
        companies = LogisticCompanySerializer(data=companies, many=True)
        serialized_data = companies.data
        return serialized_data

    def companies_price(self):
        companies_price = LogisticPrice.objects.all()
        companies_price = LogisticPriceSerializer(data=companies_price, many=True)
        serialized_data = companies_price.data
        return serialized_data

    def rider(self):
        riders = Rider.objects.all()
        riders = RidersSerializer(data=riders, many=True)
        serialized_data = riders.data
        return serialized_data

    def location(self):
        dispatch = Location.objects.all()
        dispatch = LocationSerializer(data=dispatch, many=True)
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

    def company(self):
        company = LogisticCompanySerializer(data=self.company)
        serialized_data = company.data
    def companies_price(self):
        companies_price = LogisticPrice.objects.get(company=self.company)
        companies_price = LogisticPriceSerializer(data=companies_price)
        serialized_data = companies_price.data
        return serialized_data

    def location(self):
        locations = Location.objects.filter(company=self.company)
        locations = LocationSerializer(data=locations, many=True)
        serialized_data = locations.data
        return serialized_data

