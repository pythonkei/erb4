# urls.py main function is routing and categorize

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Base on Endpoint named as (''): Empty string as reg name,
    # then run views.py Httpresponse function to response coming user request.
]


