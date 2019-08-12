from django.contrib import admin
from empMast import models


class RegistrationModelAdminClass(admin.ModelAdmin):
    list_display = ['id','userName','password']
admin.site.register(models.RegistrationModelClass,RegistrationModelAdminClass)


class UserModelAdminClass(admin.ModelAdmin):
    list_display = ['name','email_id','password','image','phone','address']
admin.site.register(models.UserModelClass,UserModelAdminClass)