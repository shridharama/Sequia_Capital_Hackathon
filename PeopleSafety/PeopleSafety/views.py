from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.utils import simplejson

import datetime

def hello(request):
    return HttpResponse("Hello world")

def search_form(request):
    return render(request, 'search_form.html')

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date':now}))
    #return HttpResponse(html)
    return render(request, 'current_datetime.html', {'current_date':now})

def search(request):
    name = "Gaurab"
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = "You entered an empty form"
    return render(request, 'search.html', {'hello':message})

def sampleMap(request):
    latitude = 20.9667
    longitude = -20.5667
    latlonlist = [[12.9667,77.5667], [18.9750,72.8258], [22.5667,88.3667], [28.6100,77.2300]]
    heatMapData = [
    [8.8678, 76.5623],
    [9.5674, 77.5623],
    [10.7821, 78.447],
    [12.4523, 79.443],
    [37.782, -122.441],
    [37.782, -122.439],
    [37.782, -122.435],
    [37.785, -122.447],
    [37.785, -122.445],
    [37.785, -122.441],
    [37.785, -122.437],
    [37.785, -122.435]]
    js_latitude = simplejson.dumps(latitude)
    js_longitude = simplejson.dumps(longitude)
    js_latlonlist = simplejson.dumps(heatMapData)
    return render(request, 'testMap.html',
                            {'LatLong':js_latlonlist,
                            'latitude':js_latitude,
                            'longitude':js_longitude}
                 )