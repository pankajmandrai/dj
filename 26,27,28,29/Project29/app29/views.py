from django.core.paginator import Paginator
from django.shortcuts import render
from .models import EmployeeModel



def show(request):
    pno = request.GET.get("page_no")
    qs = EmployeeModel.objects.all()
    p = Paginator(qs, 3,1)
    if pno:
        pge = p.page(pno)
    else:
        pge = p.page(1)

    return render(request,"index.html",{"page":pge})