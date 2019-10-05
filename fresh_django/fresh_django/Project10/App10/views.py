from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")


def validate(request):

    res = request.POST.get("t1")
    print((res))
    if(res == "yes"):
        d1 = {"msg":"Yes"}
        return render(request,"index.html",d1)
    elif(res == "no"):
        d1 = {"msg": "No"}
        return render(request, "index.html",d1)
    elif(res == "maybe"):
        d1 = {"msg": "May Be"}
        return render(request, "index.html",d1)
    else:
        d1 = {"msg": "Please select one option"}
        return render(request, "index.html", d1)


def lang(request):
    result = request.POST.get("lang")
    d1 = {"res":result}
    return render(request,"index.html",d1)


def langs(request):
    res = request.POST.getlist("langs")
    d1 = {"options":res}
    return render(request,"index.html",d1
                  )