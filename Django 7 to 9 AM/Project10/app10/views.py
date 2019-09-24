from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def readData(request):
    idno = request.POST.get("t1")
    name = request.POST.get("t2")
    salary = request.POST.get("t3")
    print(idno)
    print(name)
    print(salary)
    return None