from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import AirportModel
from .models import UrbanAreaModel
from .models import WorldBorderModel

class ReadOnlyGeom(LeafletGeoAdmin):
	readonly_fields = ('geom', )

admin.site.register(AirportModel, admin.OSMGeoAdmin )
admin.site.register(UrbanAreaModel, admin.OSMGeoAdmin)
admin.site.register(WorldBorderModel, admin.OSMGeoAdmin)
#admin.site.register(WorldBorder, admin.OSMGeoAdmin)


