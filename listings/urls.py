from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'), 
    # Python list function and data type integer variable, listing_id as integer base on database record
    # This line mean : First check listing(3) with int:id(1), then combine url endpoint into listing function(2)
    path('search', views.search, name='search'),
]
