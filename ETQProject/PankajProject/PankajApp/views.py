from django.shortcuts import render
from PankajApp import models

# Create your views here.
def showRegistrationPage(request):
    if(request.method == 'GET'):
        return render(request, 'PankajApp/registration.html')

    if(request.method == 'POST'):
        username = request.POST.get('uname')
        password = request.POST.get('password')
        models.RegistrationModelClass.objects.get_or_create(userName=username,password=password)
        return render(request,'PankajApp/login.html')


def validateUser(request):
    if(request.method == 'POST'):
        toggle = 2
        uname = request.POST.get('uname')
        upass = request.POST.get('password')
        allData = models.RegistrationModelClass.objects.all()
        for x in allData:
            if((x.userName == uname) and (x.password == upass)):
                toggle = 1
                break

        if(toggle == 1):
            return render(request, 'PankajApp/2page.html')

        else:
            myDict = {'errorMessage':'Invalid Credentials','color':'red'}
            return render(request, 'PankajApp/login.html',context=myDict)

def server(request):
    res = request.POST.getlist("server")
    d1 = {"options":res}
    return render(request,"PankajApp/home.html",d1)

def pageUser(request):
    return render(request,"PankajApp/home.html")

def homeView(request):
    return render(request,"PankajApp/home.html")

def userView(request):
    return render(request, 'PankajApp/user.html')

def mappingView(request):
    return render(request, 'pankajApp/mapping.html')

def etqView(request):
    return render(request, 'PankajApp/etq.html')

def schedulerView(request):
    return render(request, 'PankajApp/scheduler.html')

def batchView(request):
    return render(request, 'PankajApp/batch.html')





