from django.contrib import admin
from guideline.models import Patientdata, Recommendations, Patientguidelines
# Register your models here.

from guideline import models
# Register your models here.
#from PatientDataClass.models import PatientdataClass

#class PatientDataAdminClass(admin.ModelAdmin):
 #   list_display = ['name', 'gender', 'date']

admin.site.register(Patientdata)
admin.site.register(Patientguidelines)
admin.site.register(Recommendations)




