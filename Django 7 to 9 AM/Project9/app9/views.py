from django.shortcuts import render
from django.http import HttpResponse

def openIndex(request):
    return render(request,"index.html")

def readData(request):
    idno = request.POST.get("t1")
    name = request.POST.get("t2")
    salary = request.POST.get("t3")

    message = "Employee Details "+idno+name+salary

    return  HttpResponse(message)