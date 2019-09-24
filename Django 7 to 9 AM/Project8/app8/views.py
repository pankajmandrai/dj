from django.shortcuts import render

def showIndex(req):
    employee_info = {
        "101": {"name": "Ravi", "salary": 185000.00},
        "102": {"name": "kumar", "salary": 225000.00},
        "103": {"name": "shiva", "salary": 15000.00},
        "104": {"name": "mohan", "salary": 100000.00},
        "105": {"name": "murali", "salary": 15000.00},
        "106": {"name": "krishna", "salary": 18000.00},
        "107": {"name": "Prasad", "salary": 85000.00},
        "108": {"name": "Anil", "salary": 5000.00},
        "109": {"name": "Sunil", "salary": 185000.00},
        "110": {"name": "Myki", "salary": 000.00},
    }
    return render(req,"index.html",{"data":employee_info})
