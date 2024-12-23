from django.contrib import admin
from .models import Realtor
# Register your models here.

# Admin CMS in Realtor display and setting
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date') # Show field
    list_display_links = ('id', 'name') # Field can link
    search_fields = 'name', # Search function by NAME
    list_per_page = 25 # show page

admin.site.register(Realtor, RealtorAdmin)