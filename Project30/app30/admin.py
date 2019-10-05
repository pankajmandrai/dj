from django.contrib import admin
from app30 import models
#from .models import ProductModelClass

# Register your models here.
class ProductModelAdminClass(admin.ModelAdmin):
    list_display = ['name', 'price','image','quantity']
admin.site.register(models.Product,ProductModelAdminClass)


#admin.site.register(ProductModelClass)

