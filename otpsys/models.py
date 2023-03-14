# Create your models here.
from django.db import models


class Customer(models.Model):
    id = models.AutoField
    mobile_number = models.CharField(max_length=13, db_index=True)
    otp = models.CharField(max_length=6, db_index=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.mobile_number
