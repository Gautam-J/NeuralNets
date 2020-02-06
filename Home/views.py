from django.views.generic import ListView, TemplateView
from .models import Service

import json
from django.http import HttpResponse

# might have to change all views to CreateListView to use the search bar???


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
    paginate_by = 10


class SearchResultsView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'Home/search.html'

    def get_queryset(self):
        if len(self.args) > 0:
            return Service.objects.filter(title__icontains=self.args[0])
        else:
            return Service.objects.all()


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
