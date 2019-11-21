from django.shortcuts import render
from django.views.generic import FormView
from .forms import EmployeeForm

class ShowIndex(FormView):
    template_name = "index.html"
    form_class = EmployeeForm