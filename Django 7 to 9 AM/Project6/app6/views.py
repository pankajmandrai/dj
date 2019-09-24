from django.shortcuts import render

def show(request):
    student_info = {
        "rno":101,
        "name":"Ravi",
        "marks":[45,95,78,15,95,65]}

    return render(request,"index.html",student_info)