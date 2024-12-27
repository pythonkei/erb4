from django.shortcuts import render, get_object_or_404
from .models import Listing # This is Database name Listing *upcase
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, bedroom_choices, district_choices

# Use for seprate page show more record in database

# Create your views here.
def index(request):
    listings = Listing.objects.all() # Create variable listings for load all record from Database
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) 
    # ('-list_date') inside (-) mean show Lastest input record, that mean recent record,
    # filter out is_published uncheck box from CMS, use for not display in list

    paginator = Paginator(listings,3) # Paginator function by line 3, 3 value is how number show record
    page = request.GET.get('page') # page variable decele, ('page') is parameter for html call url ?page={{i}}
    paged_listings = paginator.get_page(page) # Paginator function for seperate page
    context = {
        'listings' : paged_listings,
    }
    # This line mean : "variable" : "value", context variable
    # Use python DICT function method packageing all record to template html
    return render(request,'listings/listings.html', context)

def listing(request, listing_id):
    # listing_id active while initial here
    # function from urls.py: path('<int:listing_id>', views.listing, name='listing')
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing' : listing } #Check record exsiting or not, if no record go to 404 page
    return render(request,'listings/listing.html', context)

# Second filter function using queryset and which datatype set option
# Search Logic: get keywords depend on user input, then build queryset to queryset_list variable in context,
# then assign result to search.html and continuous to second search or filter by field button.

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords'] 
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords) 

    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains = title)

    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            if district != '_':
                queryset_list = queryset_list.filter(district__iexact = district)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte = bedrooms) #lte as internal function mean lower than and equal to

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)

    context = {
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'district_choices':district_choices,
        'listings':queryset_list,
        'values' : request.GET, # request.GET as variable: values for index search function call
    }
    return render(request,'listings/search.html',context)