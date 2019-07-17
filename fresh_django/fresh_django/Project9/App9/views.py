from django.shortcuts import render
def showIndex(request):
    return render(request,"index.html")


def validate(request):
    result = request.POST.getlist("cb")
    if(len(result) == 0):
        message = "Please select atleast one language."
        d1 = {"msg":message,"color":"red"}
        return render(request, "index.html",d1)
    else:
        d1 = {"result":result}
        return render(request,"details.html",d1)