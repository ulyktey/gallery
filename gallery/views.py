from django.template.loader import get_template
from django.http import HttpResponse
from django.http import Http404
from django import template
from django.views.decorators.csrf import csrf_exempt
#import json
#import os
import logging
#from location.models import Region, City
#import parse_content

log = logging.getLogger(__name__)
def home(request):
    log.info('Test bjfjdskfjd ====')
    log.debug('ajsdhjsadsa====1111111')
    return HttpResponse('home')
