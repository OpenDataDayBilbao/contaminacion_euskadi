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


limits = {
    'Benzene': 0,
    'CO': 10000,
    'Ethylbenzene': 0,
    'NH3': 0,
    'NMHC': 0,
    'PM10': 50,
    'SH2': 0,
    'Toluene': 0,
    'Xylene': 0,
}


def home(request):
    points = []
    if request.method == 'POST':
        form = ParticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            particle = cd['particle']
            start_date = cd['start_date']
            end_date = cd['end_date']

            json_response = json.load(urllib2.urlopen('http://helheim.deusto.es/bizkaisense/api/outlimit_stations/' + particle + '/' + start_date + '/' + end_date + '/' + str(limits[particle]) + ''))

            municipios = AirPollution.objects.filter(descripcion = particle).values('municipio')

            for element in json_response:
                found = False
                for mun in municipios.values():
                    found = found or (mun['municipio'] == element['municipality'])
                if found:
                    points.append(element)

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
