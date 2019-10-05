from django.contrib import admin
from PankajApp import models

class RegistrationModelAdminClass(admin.ModelAdmin):
    list_display = ['id','userName','password']
admin.site.register(models.RegistrationModelClass,RegistrationModelAdminClass)


class FromModelAdminClass(admin.ModelAdmin):
    list_display = ['user_id','first_name','middle_name','last_name','full_name','gender','email_address','user_name','user_password','is_active',
                    'start_date','end_date','created_by','creation_date','last_updated_by','last_updated_date']
admin.site.register(models.FromModelClass,FromModelAdminClass)