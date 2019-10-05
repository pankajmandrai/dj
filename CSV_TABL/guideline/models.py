from django.db import models

class Patientdata(models.Model):
    GENDER = (('m', 'Male'), ('f', 'Female'))

    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True,db_index=True)
    gender = models.CharField(max_length=1, choices=GENDER, null=True)
    systolic_BP = models.PositiveIntegerField(default=0)
    diastolic_BP = models.PositiveIntegerField(default=0)
    smoking_years = models.PositiveIntegerField(default=0)
    no_of_packs = models.PositiveIntegerField(default=10)
    fasting_blood_sugar = models.PositiveIntegerField(default=10)
    hypothyroid = models.BooleanField(default=True)
    obese = models.BooleanField(default=False)
    intravenous_drug_abuse = models.BooleanField(default=False)

class Patientguidelines(models.Model):
    patient = models.CharField(max_length=30)

class Recommendations(models.Model):
    name = models.CharField(max_length=30)
    recommendation= models.CharField(max_length=30)
    conditions= models.CharField(max_length=30)
    references = models.CharField(max_length=30)

    def __str__(self):
        return "%s" % self.id