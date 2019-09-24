from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def showFun(request):
    if request.method == "POST":
        upass = request.POST.get("t1")
        print(upass)
        return HttpResponse("Post is Clicked")
    else:
        upass = request.POST.get("t2")
        print(upass)
        return HttpResponse("Get is Clicked")
