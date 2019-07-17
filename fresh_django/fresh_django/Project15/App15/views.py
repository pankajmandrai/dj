from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def hero(request):
    langs = request.GET.get("hero")
    return render(request,"index.html",{"hero":langs})