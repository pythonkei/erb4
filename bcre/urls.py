"""
URL configuration for bcre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# urls.py main function is GLOBAL routing and categorize,
# then to pages/urls.py for sub routing and sub categorize (line 26)


# from django that mean library, import is shortcut or label name
from django.contrib import admin # Project demo new added
from django.urls import path,include # Project demo new added
from django.conf.urls.static import static # Project demo new added
from django.conf import settings # Project demo new added
from debug_toolbar.toolbar import debug_toolbar_urls


# Endpoint Define and traffic heavy ratio
urlpatterns = [
   path('', include ('pages.urls')), # this line is project added
   path('listings/', include ('listings.urls')),
   path('contacts/', include ('contacts.urls')),
   path('accounts/', include ('accounts.urls')),
   # Serve end user 95% traffic first, '': Empty string for path categorize -> urls.py to pages folder
   path('admin/', admin.site.urls) #  Path endpoint as 'admin/' this line is (Project new added)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls() # Define path to store photo from dynamic to static, Variable from settings.py
