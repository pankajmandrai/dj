from django.shortcuts import render
def showIndex(request):

    return render(request,"index.html")


def validate(request):
    uname = request.POST.get("t1")
    upass = request.POST.get("t2")
    type1 = request.POST.get("btn")
    if(uname == "" or upass == "" or type1 == None):
        error = "Please fill all details."
        d1 = {"msg":error}
        return render(request, "index.html",d1)
    else:
        if(uname == "admin" and upass =="ADMIN" and type1 == "Admin"):
            d1 = {"type":type1}
            return render(request,"admin.html",d1)

        elif(((uname == "client1" and upass == "c1") or (uname == "client2" and upass == "c2")) and type1 == "Client"):
            if(uname == "client1"):
                d1 = {"type": "Client-1"}
                return render(request, "client.html", d1)
            else:
                d1 = {"type": "Client-2"}
                return render(request, "client.html", d1)

        elif (((uname == "emp1" and upass == "one") or (uname == "emp2" and upass == "two")) and type1 == "Emplyoee"):
            if (uname == "emp1"):
                d1 = {"type": "Emplyoee-1"}
                return render(request, "emp.html", d1)
            else:
                d1 = {"type": "Emplyoee-2"}
                return render(request, "emp.html", d1)
        else:
            error = "Please enter valid credentials."
            d1 = {"msg": error}
            return render(request, "index.html", d1)
