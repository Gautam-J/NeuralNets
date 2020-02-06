from django.views.generic import ListView
from .models import Service

import json
from django.http import HttpResponse


class ServicesView(ListView):
    model = Service
    template_name = 'Home/home.html'
    context_object_name = 'services'
    ordering = ['-pk']


# for autocomplete on the search field in navbar
def get_services(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        services = Service.objects.filter(title__icontains=q)
        results = []
        for ser in services:
            ser_json = {}
            ser_json = ser.title
            results.append(ser_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
