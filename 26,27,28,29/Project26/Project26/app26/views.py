from django.shortcuts import render
from .forms import EmployeeForm

def showIndex(request):
    ef = EmployeeForm()
    return render(request,"index.html",{"form":ef})