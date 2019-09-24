from django.shortcuts import render
from .models import SavingsAccount


def showIndex(request):
    return render(request,"index.html")

def createNewAccount(request):
    return render(request,"createnewaccount.html")

def saveAccount(request):
    account_no = request.POST.get("acno")
    name = request.POST.get("name")
    open_balance = request.POST.get("ob")
    upass = request.POST.get("password")

    sa = SavingsAccount(acno = account_no,name=name,balacne=open_balance,password=upass)
    sa.save()
    return render(request,"index.html",{"message":"Account Created"})