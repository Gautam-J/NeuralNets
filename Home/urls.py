from django.urls import path
from .views import ServicesView, get_services

urlpatterns = [
    path('', ServicesView.as_view(), name='home-view'),
    path('ajax_calls/myFunction', get_services, name='get_services'),
]
