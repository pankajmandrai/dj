from django.shortcuts import render
from django.views.generic import CreateView
from .models import EmployeeReg

class EmployeeRegFormView(CreateView):
    model = EmployeeReg
    fields = ["name","age","contact","email","password"]
    template_name = "index.html"
