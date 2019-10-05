from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def validate(request):
    res = request.POST.getlist("hero")
    if(len(res)>6):
        message = "Please select upto 6 images only ..!"
        d1 = {"msg":message,"color":"red"}
        return render(request,"index.html",d1)
    elif(len(res) == 0):
        message = "Please select atleast 1 image..!"
        d1 = {"msg": message, "color": "red"}
        return render(request, "index.html", d1)
    else:
        res = request.POST.getlist("hero")
        d1 = {"heros":res}
        return render(request,"details.html",d1)