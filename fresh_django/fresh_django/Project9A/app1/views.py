from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")


def display(request):
    name = request.POST.get("b1")
    return render(request,"hero.html",{"image":name})


def search(request):
    name=request.POST.get("t1")
    return render(request,"display.html",{"message":name})