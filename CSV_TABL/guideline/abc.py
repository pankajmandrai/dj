import csv

from guideline.models import Patientdata, Patientguidelines, Recommendations

with open('Patient_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    next(csv_reader)

    for row in csv_reader:
        date, name, gender,systolic_BP,diastolic_BP,smoking_years,no_of_packs,fasting_blood_sugar,hypothyroid,obese,intravenous_drug_abuse= row
    print(row)
csv_file.close()


import csv
from django.http import HttpResponse,admin
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj,field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Patientdata)
class PatientdataAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("name", "date", "gender", "systolic_BP", "diastolic_BP", "smoking_years", "no_of__packs", "fasting_blood_sugar", "hypothyroid",
                    "obese","intravenous_drug_abuse")
    list_filter = ("name")
    actions = ["export_as_csv"]

@admin.register(Patientguidelines)
class PatientguidelinesAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("name")
    actions = ["export_as_csv"]


@admin.register(Recommendations)
class RecommendationsAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("name", "recommendation", "conditions","references")
    actions = ["export_as_csv"]