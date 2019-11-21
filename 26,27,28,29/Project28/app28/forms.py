from django import forms
from .models import EmployeeModel

# class EmployeeForm(forms.Form):
#     idno = forms.IntegerField()
#     name = forms.CharField()
#     salary = forms.FloatField()
#     password = forms.CharField(max_length=8,widget=forms.PasswordInput)
#

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"
        #fields = ("idno","salary")
