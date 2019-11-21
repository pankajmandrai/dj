
from django import forms

class EmployeeForm(forms.Form):
    f_idno = forms.IntegerField(help_text="Must be 3 Digits")
    f_name = forms.CharField()
    f_salary = forms.FloatField()