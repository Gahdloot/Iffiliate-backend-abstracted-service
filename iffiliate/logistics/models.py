from django.db import models
from decimal import Decimal
# Create your models here.


class LogisticCompany(models.Model):
    name = models.CharField(max_length=240)
    phone_number = models.IntegerField(default=0)
    address = models.TextField()


class LogisticPrice(models.Model):
    """
    THIS IS THE PRICING MODEL OF THE COMPANY BASED ON WEIGHT AND AND VALUE OF PRODUCT
    OPERATION TO BE TAKEN ARE AS FOLLOWED
    ((value_per_goods * value of goods) + (price_per_weight * weight of product))
    """
    company = models.OneToOneField(LogisticCompany, on_delete=models.CASCADE)
    value_per_goods = models.DecimalField(max_digits=5, decimal_places=2, default=0.01)
    price_per_weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.01)
    #
    # @property
    # def price(self, value, weight):
    #     value_per_goods = float(self.value_per_goods) * float(value)
    #     return self.price_per_weight - self.value_per_goods


class Dispatch(models.Model):
    """
    this collect the price per location of specific companies
    """
    company = models.ForeignKey(LogisticCompany, on_delete=models.CASCADE)
    country = models.CharField(max_length=75)
    state = models.CharField(max_length=75)
    city = models.CharField(max_length=75)
    price = models.IntegerField(default=0)


class Rider(models.Model):
    """
    when an order is booked a dispatch rider from the model holds the information of the dispatch
    """
    company = models.ForeignKey(LogisticCompany, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    number = models.IntegerField(default=0)