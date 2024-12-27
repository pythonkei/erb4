from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, district_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings' : listings,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'district_choices':district_choices,
    }
    return render(request,'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date') # order_by -hire _date mean recent date
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True) # Enable mvp realtors and active by CMS
    context = {  # This mean: context as package list variable with sub 2 variable for check
        'realtors' :realtors,
        'mvp_realtors' : mvp_realtors
    }
    return render(request,'pages/about.html', context) # put context variable into about.html

# def search(request):
#     context = {
#         'price_choices':price_choices,
#         'bedroom_choices':bedroom_choices,
#         'district_choices':district_choices,
#     }
#     return render(request,'listings/search.html', context)