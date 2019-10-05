from django.db import models


class StudentModel(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    faculty_name = models.CharField(max_length=30)
    fees = models.DecimalField(max_digits=7,decimal_places=2)
    time = models.TimeField()

