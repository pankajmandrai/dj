from django.db import models

class SavingsAccount(models.Model):
    acno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    balacne = models.DecimalField(max_digits=10,decimal_places=2)
    password = models.CharField(max_length=30)