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


# Project demo added:
from django.contrib import admin # Project demo new added:
from django.urls import path,include # Project demo new added:

urlpatterns = [
   path('', include ('pages.urls')), # Project demo added:
   # Serve end user 95% traffic first, '': Empty string for path categorize -> urls.py to pages folder
   path('admin/', admin.site.urls) # Project demo added:
]

