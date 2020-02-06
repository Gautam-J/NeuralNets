from django.urls import path
from .views import ServicesView, get_services, AboutView, ContactView, ListAllModelsView

urlpatterns = [
    path('', ServicesView.as_view(), name='home-view'),
    path('ajax_calls/myFunction', get_services, name='get_services'),
    path('about/', AboutView.as_view(), name='about-view'),
    path('contact/', ContactView.as_view(), name='contact-view'),
    path('models/', ListAllModelsView.as_view(), name='listmodels-view'),
]
