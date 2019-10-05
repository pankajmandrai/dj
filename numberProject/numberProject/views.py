from datetime import datetime
from django.shortcuts import render
from django.views.generic.base import View
from num2words import num2words
from django.http import HttpResponse
import json
class ShowTextString(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {'textNumber': ''})

    def post(self, request, *args, **kwargs):
        number = request.POST['number']
        textNumber = num2words(number, to='cardinal', lang='en_IN')

        return HttpResponse(json.dumps({'number': number, 'textNumber': textNumber}), content_type='application/json')

