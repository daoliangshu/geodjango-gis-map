from django.contrib.gis import admin
from .models import AirportModel
from .models import UrbanAreaModel
from .models import WorldBorderModel
from .models import AdminBoundaryModel

admin.site.register(AirportModel, admin.OSMGeoAdmin )
admin.site.register(UrbanAreaModel, admin.OSMGeoAdmin)
admin.site.register(WorldBorderModel, admin.OSMGeoAdmin)
admin.site.register(AdminBoundaryModel, admin.OSMGeoAdmin)


