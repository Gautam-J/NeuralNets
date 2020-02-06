from django.urls import path
from .views import CreateIrisDataView

urlpatterns = [
    path('', CreateIrisDataView.as_view(), name='iris-predict'),
]
