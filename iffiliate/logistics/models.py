from django.db import models

#from iffiliate.vendor.models import Vendor


import logging
from decimal import Decimal
# Create your models here.


class LogisticCompany(models.Model):
    name = models.CharField(max_length=240)
    phone_number = models.CharField(max_length=240, null=True, blank=True)
    address = models.TextField()


class LogisticPrice(models.Model):
    """
    THIS IS THE PRICING MODEL OF THE COMPANY BASED ON WEIGHT AND VALUE OF PRODUCT
    OPERATION TO BE TAKEN ARE AS FOLLOWED
    ((value_per_goods * value of goods) + (price_per_weight * weight of product))
    """
    company = models.OneToOneField(LogisticCompany, on_delete=models.CASCADE)
    value_per_goods = models.DecimalField(max_digits=5, decimal_places=2, default=0.01)
    price_per_weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.01)
    def price(self, value, weight):
        total_value = self.value_per_goods * value
        total_weight = self.price_per_weight * weight
        return total_value + total_weight


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




class DispatchedOrder(models.Model):
    #this is supposed to cover the vendor information
    #order = models.ForeignKey(Vendor, on_delete=models.CASCADE())
    company = models.ForeignKey(LogisticCompany, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
