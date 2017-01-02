from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from . import forms
from . import models
from django.core.urlresolvers import reverse
from django.core.serializers import serialize
import datetime
#from .forms import OsmPolygonWidget


def display_form(request):
    if request.method=='POST':
        form = forms.ChooseCountryForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])
            country = models.WorldBorderModel.objects.filter(id=request.POST['name'])
            print(country[0].get_geom().centroid)
            return HttpResponseRedirect(reverse('home')+'?country_id=%s&display_mode=%s' \
                                       %(request.POST['name'], request.POST['result_mode']))
    else:

        form = forms.ChooseCountryForm()
        return render(request, 'world/display_form.html',
                    {'display_form' : form})

def get_serealize(request):
    country_id = request.GET.get('country_id', 30)
    display_mode = (int)(request.GET.get('display_mode', 1))
    country_to_search = 'France'
    if country_id is not None:
        country_to_search = models.WorldBorderModel.objects.get(id=country_id).get_name()
    subres = models.WorldBorderModel.objects.get(id=country_id).get_geom()
    data = None
    if display_mode == 1:
        """ Display Urban Areas in selected country """
        max_area = models.UrbanAreaModel.objects.order_by("-area_sqkm")[0].\
                        area_sqkm
        max_area /= 4

        #only choose 150 bigger area
        data = models.UrbanAreaModel.objects.filter(geom__intersects=subres).\
                                          order_by("-area_sqkm")[:150]
        jsonized = serialize('geojson', data,
                    geometry_field='geom',
                    fields=('area_sqkm',)
                )

    elif display_mode == 2:
        data = models.AirportModel.objects.filter(geom__within=subres)
        jsonized = serialize('geojson', data,
                    geometry_field='geom',
                    fields=('name',)
                )
    elif display_mode == 3:
        data = models.AdminBoundaryModel.objects.exclude(geom__disjoint=subres).\
                                            filter(geom__bboverlaps=subres).\
                                                order_by("-labelrank")[:150]
        jsonized = serialize('geojson', data,
                    geometry_field='geom',
                    fields=('name', ),
                )
    elif display_mode == 4:
        data = models.WorldBorderModel.objects.filter(id=country_id)
        jsonized = serialize('geojson', data,
                    geometry_field='geom',
                    fields=('name',)
                )        
    # max_area = get_max_urban_area_in_country(str(subres))
    # data = get_urbans_in_country_lt(str(subres), max_area )
    res = jsonized
    return HttpResponse(res, content_type='text/javascript')


def get_max_urban_area_in_country(container_geom):
    query = 'SELECT "world_urbanareamodel"."id", ST_Area("world_urbanareamodel"."geom") FROM ' + \
            'world_urbanareamodel ' +\
            'WHERE ST_Contains("world_urbanareamodel"."geom",ST_GeometryN(%(geo)s ,1)) ' +\
            'ORDER BY ST_Area("world_urbanareamodel"."geom") DESC LIMIT 1;'
    
    top_area = models.UrbanAreaModel.objects.raw(query, {'geo' : container_geom})
    for area in top_area:
        return area

def get_urbans_in_country_lt(container_geom, max_area):
    query = 'SELECT "world_urbanareamodel"."id", "world_urbanareamodel") FROM ' + \
            'world_urbanareamodel ' +\
            'WHERE ST_Contains("world_urbanareamodel"."geom",ST_GeometryN(%(geo)s ,1)) ' +\
            'AND ST_Area("world_urbanareamodel"."geom") <= %(bound)s ' +\
            'ORDER BY ST_Area("world_urbanareamodel"."geom") DESC LIMIT 1;'
    res = models.UrbanAreaModel.objects.raw(query, {'geo' : container_geom, 'bound' : max_area})
    return res
