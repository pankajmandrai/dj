from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView
from .models import Product

class SaveDetails(View):
    def post(self,request):
        name = request.POST.get("t1")
        price = request.POST.get("t2")
        quantity = request.POST.get("t3")
        image = request.POST.get("t4")

        pro = product(name=name,price=price,quantity=quantity,image=image)
        pro.save()
        return render(request,"index.html",{"message":"Data Saved"})

class ViewAllProduct(ListView):
    model = Product