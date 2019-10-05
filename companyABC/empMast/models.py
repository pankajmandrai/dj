from django.db import models
from phone_field import PhoneField
class RegistrationModelClass(models.Model):
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

class UserModelClass(models.Model):
    #user_id = models.PositiveIntegerField(blank=True)
    name = models.CharField(max_length=30)
    image = models.ImageField()
    email_id = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    phone = models.PositiveIntegerField()
   # phone = PhoneField(blank=True, help_text='Contact phone number')
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.id