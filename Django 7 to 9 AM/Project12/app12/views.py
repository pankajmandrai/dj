from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def sendData(request):
    i = request.POST.get("idno")
    n = request.POST.get("name")
    c = request.POST.get("contact")
    e = request.POST.get("email")
    g = request.POST.get("gender")

    l1 = request.POST.get("c")
    l2 = request.POST.get("c++")
    l3 = request.POST.get("python")
    l4 = request.POST.get("django")
    l5 = request.POST.get("project")

    ts = [l1,l2,l3,l4,l5]

    f = request.POST.get("faculty")

    d1 = {
        "idno":i,
        "name":n,
        "contact":c,
        "email":e,
        "gender":g,
        "ts":ts,
        "faculty":f
    }


    return render(request,"show.html",d1)



# "c":l1,
#         "c++":l2,
#         "python":l3,
#         "django":l4,
#         "project":l5