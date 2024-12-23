from django.shortcuts import render
from .models import Listing # This is Database name Listing *uppcase
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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
        'listings' : paged_listings
    }
    # This line mean : "variable" : "value", context variable
    # Use python DICT function method packageing all record to template html
    return render(request,'listings/listings.html', context)

def listing(request, listing_id): 
    # listing_id active while initial here
    # function from urls.py: path('<int:listing_id>', views.listing, name='listing')
    return render(request,'listings/listing.html')

def search(request):
    return render(request,'listings/search.html')