from django.shortcuts import render

def showLogin(request):
    return render(request,"login.html")


def validate(request):
    uname = request.POST.get("t1")
    upass = request.POST.get("t2")

    if(uname == "admin" and upass == "admin"):
        return render(request,"admin.html")

    elif(uname == "ravi" and upass == "kumar"):
        return render(request, "employee.html")

    elif (uname == "mohan" and upass == "bhargav"):
        return render(request, "employee.html")

    elif (uname == "user1" and upass == "one"):
        return render(request, "user.html")

    elif (uname == "user2" and upass == "two"):
        return render(request, "user.html")

    else:
        return render(request, "login.html",{"message":"Invalid Credentials"})