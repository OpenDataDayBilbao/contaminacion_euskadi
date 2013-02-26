# coding: utf-8

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

import json

import urllib2

from app.models import AirPollution
from app.forms import ParticleForm


def home(request):
    points = []
    limit = '0'
    if request.method == 'POST':
        form = ParticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            particle = cd['particle']
            start_date = cd['start_date']
            end_date = cd['end_date']

            if particle == 'SO2':
                limit = '125'
            if particle == 'NO2':
                limit = '200'
            if particle == 'PM10':
                limit = '50'
            if particle == 'CO':
                limit = '10'

            json_response = json.load(urllib2.urlopen('http://helheim.deusto.es/bizkaisense/api/outlimit_stations/' + particle + '/' + start_date + '/' + end_date + '/' + limit + ''))

            municipios = AirPollution.objects.filter(descripcion=particle).values('municipio')

            for element in json_response:
                print element['municipality']
                #if str(element['municipality']) in municipios.values():
                    #points.append(element)
                found = False
                for mun in municipios.values():
                    print "--->", mun['municipio']
                    found = found or (mun['municipio'] == element['municipality'])
                if found:
                    points.append(element)

            print '------------------------------------'
            print municipios
            print '------------------------------------'
            print points

            return render_to_response("app/index.html", {
                    'form': form,
                    'points': points,
                },
                context_instance=RequestContext(request))

    else:
        form = ParticleForm()

    return render_to_response("app/index.html", {
            'form': form,
            'points': points,
        },
        context_instance=RequestContext(request))
