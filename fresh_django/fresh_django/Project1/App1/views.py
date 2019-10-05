from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def validate(request):
    uname = request.POST.get("t1")
    upass = request.POST.get("t2")
    if uname == "sathya" and upass == "tech":
        message = "Valid user"
        return render(request, "index.html",{"mess":message})
    else:
        message = "Invalid user"
        return render(request, "index.html", {"mess": message})



