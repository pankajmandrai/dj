from django.http import HttpResponse
def wish(request):
    html_code = "<html><body bgcolor='yellow'><h1>Good Morning Django</h1></body></html>"
    return HttpResponse(html_code)    
