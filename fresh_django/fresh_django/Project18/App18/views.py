from django.shortcuts import render
from .models import Student
# Create your views here.
def showIndex(request):
    res = Student.objects.all()
    print(res)
    return render(request,"index.html")

def saveDetails(request):
    namep = request.POST.get("name")
    agep = request.POST.get("age")
    cnop = request.POST.get("cno")
    genderp = request.POST.get("gender")
    addressp = request.POST.get("address")
    statep = request.POST.get("state")
    languagesp = request.POST.getlist("cb1")

    e1 = Student(name=namep,age=agep,cno=cnop,gender=genderp,address=addressp,state=statep,languages=languagesp)
    e1.save()
    return render(request,"index.html")