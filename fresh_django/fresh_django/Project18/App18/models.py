from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    cno = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    languages = models.CharField(max_length=100)

