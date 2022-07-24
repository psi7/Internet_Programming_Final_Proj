from django.http import (
    Http404,
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseBadRequest,
)
from django.shortcuts import render
from django.http import HttpResponse
from events.models import Events,Users,Location
from django import forms
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)


def contact(request):
    ...
    logger.debug("Log whatever you want")


def index(request):
    return render(request, "events/index.html", {"events": ""})
