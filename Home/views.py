from django.views.generic import ListView, TemplateView
from .models import Service

import json
from django.http import HttpResponse


class ServicesView(ListView):
    model = Service
    template_name = 'Home/home.html'
    context_object_name = 'services'
    ordering = ['-pk']
    paginate_by = 4  # only to view the latest 4 models


class AboutView(TemplateView):
    template_name = 'Home/about.html'


class ContactView(TemplateView):
    template_name = 'Home/contact.html'


class ListAllModelsView(ListView):
    model = Service
    template_name = 'Home/listmodels.html'
    context_object_name = 'services'
    ordering = ['-pk']


class SearchResultsView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'Home/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Service.objects.filter(title__icontains=query)
        return object_list


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
