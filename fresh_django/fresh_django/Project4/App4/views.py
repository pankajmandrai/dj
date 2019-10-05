from django.shortcuts import render

def showLogin(request):
    return render(request,"login.html")


def validate(request):
    uname = request.POST.get("t1")
    upass = request.POST.get("t2")

    if(uname == "admin" and upass == "admin"):
        type = "admin"
        d1 = {"type":type,"uname":uname}
        return render(request,"welcome.html",d1)

    elif (uname == "ravi" and upass == "kumar"):
        type = "Employee"
        d1 = {"type": type, "uname": uname}
        return render(request, "welcome.html", d1)

    elif (uname == "mohan" and upass == "bhargav"):
        type = "Employee"
        d1 = {"type": type, "uname": uname}
        return render(request, "welcome.html", d1)

    elif (uname == "user1" and upass == "one"):
        type = "User"
        d1 = {"type": type, "uname": uname}
        return render(request, "welcome.html", d1)

    elif (uname == "user2" and upass == "two"):
        type = "User"
        d1 = {"type": type, "uname": uname}
        return render(request, "welcome.html", d1)

    else:
        d1 = {"message":"Invalid Credentials"}
        return render(request, "login.html", d1)