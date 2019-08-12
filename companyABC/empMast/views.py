from django.shortcuts import render
from empMast import models

# Create your views here.
def showRegistrationPage(request):
    if(request.method == 'GET'):
        return render(request, 'empMast/registration.html')

    if(request.method == 'POST'):
        username = request.POST.get('uname')
        password = request.POST.get('password')
        models.RegistrationModelClass.objects.get_or_create(userName=username,password=password)
        return render(request,'empMast/login.html')


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
            return render(request, 'empMast/2page.html')

        else:
            myDict = {'errorMessage':'Invalid Credentials','color':'red'}
            return render(request, 'empMast/login.html',context=myDict)

def server(request):
    res = request.POST.getlist("server")
    d1 = {"options":res}
    return render(request,"empMast/home.html",d1)

def userView(request):
    if (request.method == 'GET'):
        return render(request, 'empMast/user.html')

    if (request.method == 'POST'):
        name = request.POST.get('name')
        password = request.POST.get('pwd')
        email_id = request.POST.get('email_id')
        image = request.POST.get('pic')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        models.RegistrationModelClass.objects.get_or_create(name=name,address=address, email_id=email_id, pic=image, phone=phone, pwd=password)
        return render(request, 'empMast/user.html')
    else:
        myDict = {'errorMessage': 'Data not saved', 'color': 'red'}
        return render(request, 'empMast/user.html', context=myDict)

def mappingView(request):
    return render(request, 'empMast/mapping.html')

def employeView(request):
    return render(request, 'empMast/employe.html')

def schedulerView(request):
    return render(request, 'empMast/scheduler.html')

def batchView(request):
    return render(request, 'empMast/batch.html')

def pageUser(request):
    return render(request,"empMast/home.html")

def homeView(request):
    return render(request,"empMast/home.html")



