from django.contrib import admin
from django.urls import path, include
import django.urls 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include("events.urls")),
]
