from .models import LogisticCompany, LogisticPrice, Location, Rider
from .serializers import LogisticCompanySerializer, LogisticPriceSerializer, RidersSerializer, LocationSerializer
# Create your views here.


class AllInfo:
    """
    Pending: to add model as a parameter
    """

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

    def locations(self):
        locations = Location.objects.filter(company=self.company)
        locations = LocationSerializer(data=locations, many=True)
        serialized_data = locations.data
        return serialized_data

    def riders(self):
        riders = Rider.objects.filter(company=self.company)
        riders = RidersSerializer(data=riders, many=True)
        serialized_data = riders.data
        return serialized_data


class Calculate_bill:

    iffiliate_comission = 300

    def __init__(self,company_name, value, weight, city):
        self.weight = weight
        self.value = value
        self.city = city
        self.name = company_name

        if company_name is None:
            raise NameError('company\'s name cannot be None ')
        try:
            company = LogisticCompany.objects.get(name=company_name)
        except LogisticCompany.DoesNotExist:
            raise LookupError('company\'s name doesnot exist')
        self.company = company

    def _get_price(self):
        _logistic_price = LogisticPrice.objects.get(company=self.company)
        logistic_price = _logistic_price.price(self.value, self.weight)
        _location_price = Location.objects.get(company=self.company, city=self.city)
        location_price = _location_price.price
        return logistic_price + location_price


    def checkout_logistics(self):

        return Calculate_bill.iffiliate_comission + self._get_price()

    @classmethod
    def change_comission(cls, comission):
        Calculate_bill.iffiliate_comission = comission
        return True

