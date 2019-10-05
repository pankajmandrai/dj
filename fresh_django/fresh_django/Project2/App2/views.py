from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def validate(request):
    uname = request.POST.get("t1")
    upass = request.POST.get("t2")
    if(upass == "123" and uname == "Rahul"):
        mes = uname
        d1 = {"message" : mes}
        return render(request, "welcome.html",d1)
    else:
        message = "Invalid user"
        d1 = {"message" : message}
        return render(request, "index.html",d1)
