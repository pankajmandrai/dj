from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    cno = models.IntegerField()
    email = models.EmailField(max_length=100)



