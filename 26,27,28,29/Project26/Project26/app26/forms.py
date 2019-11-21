from django import forms

class EmployeeForm(forms.Form):
    idno = forms.IntegerField(max_value=5000)
    f_name = forms.CharField(label="NAME")
    f_salary = forms.FloatField(label="SALARY")
    f_gender = forms.ChoiceField(label="GENDER",choices=(("MALE","male"),("FEMALE","female")),widget=forms.RadioSelect)

    values = (('Manager',"Manager"),("Designer","Designer"),("Developer","Developer"))

    f_designation = forms.ChoiceField(label="DESIGNATION",choices=values)

    f_lang1 = forms.ChoiceField(label="Python",widget=forms.CheckboxInput)
    f_lang2 = forms.ChoiceField(label="Django",widget=forms.CheckboxInput)

    f_password = forms.CharField(label="PASSWORD",widget=forms.PasswordInput,max_length=8)

