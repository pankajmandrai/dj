from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")


def show(request):
    id = request.POST.get("t1")
    na = request.POST.get("t2")
    sal = request.POST.get("t3")

    d1 = {"idno":id,"name":na,"salary":sal}

    return render(request,"show.html",d1)