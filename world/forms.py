#import floppyforms as forms
from django.forms import MultiWidget
from django import forms
from .models import WorldBorderModel

"""
class OsmLineStringWidget(forms.gis.BaseOsmWidget,
						  forms.gis.LineStringWidget):
	pass

class OsmPolygonWidget(forms.gis.BaseOsmWidget,
					  forms.gis.PolygonField):
	pass
	
class OsmForm(forms.Form):
	line = forms.gis.LineStringField(widget=OsmLineStringWidget())
	pp = []
	polygon = forms.gis.PolygonField(widget=OsmPolygonWidget())
	

class MyGeoForm(forms.Form):
	point = forms.gis.PointField()
"""
class ChooseCountryForm(forms.Form):
	
	display_choice = (
		('1', 'Urban areas'),
		('2', 'Airports'),
		('3', 'Admin Boundaries'),
		('4', 'Country area'),
	)

	name = forms.ChoiceField(choices=[ (o.id, str(o.get_name())) for o in WorldBorderModel.objects.all()])
	result_mode = forms.ChoiceField(choices=display_choice)
	
    
	
