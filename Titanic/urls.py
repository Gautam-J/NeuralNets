from django.urls import path
from .views import CreateTitanicDataView

urlpatterns = [
    path('', CreateTitanicDataView.as_view(), name='titanic-predict'),
]
