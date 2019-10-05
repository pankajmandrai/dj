from django.http import HttpResponse
def wish(request):
    message = "Good Morning Django"
    return HttpResponse(message)
