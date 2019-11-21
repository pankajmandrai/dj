from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import EmployeeModel
from django.contrib import messages

def showIndex(request):
    ef = EmployeeForm()
    return render(request,"index.html",{"form":ef})


def saveEmployee(request):
    id = request.POST.get("f_idno")
    na = request.POST.get("f_name")
    sal = request.POST.get("f_salary")
    EmployeeModel(idno=id,name=na,salary=sal).save()
    messages.success(request,"Details are saved")
    return redirect('main')