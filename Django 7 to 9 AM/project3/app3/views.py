from django.shortcuts import render

def showWelcome(request):
    return render(request,"welcome.html")
