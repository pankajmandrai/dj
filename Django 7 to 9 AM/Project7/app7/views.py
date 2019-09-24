from django.shortcuts import render

def showIndex(request):
    employee_details = {
        "101":{"name":"Ravi","salary":185000.00},
        "102":{"name":"Kumar","salary":225000.00},
        "103":{"name":"Mohan","salary":100000.00},
        "104":{"name":"Myki","salary":120000.00},
        "105":{"name":"Rama","salary":220000.00}
    }
    return render(request,"index.html",{"data":employee_details})