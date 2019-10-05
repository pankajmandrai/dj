from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField()




