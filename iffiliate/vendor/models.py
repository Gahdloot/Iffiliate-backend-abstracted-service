from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor = models.CharField(max_length=220, null=True, blank=True)