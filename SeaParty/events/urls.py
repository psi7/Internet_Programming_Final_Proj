from django.contrib import admin
from django.urls import  path, include
from django.views.generic import ListView
import django.urls 
import logging
import traceback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include("events.urls")),
]
