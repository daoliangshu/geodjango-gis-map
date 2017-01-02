import os
from django.contrib.gis.utils import LayerMapping
from .models import AirportModel

airportmodel_mapping = {
    'scalerank' : 'scalerank',
    'featurecla' : 'featurecla',
    'type' : 'type',
    'name' : 'name',
    'abbrev' : 'abbrev',
    'location' : 'location',
    'gps_code' : 'gps_code',
    'iata_code' : 'iata_code',
    'wikipedia' : 'wikipedia',
    'natlscale' : 'natlscale',
    'geom' : 'MULTIPOINT',
}

file_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/airports', 'ne_10m_airports.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        AirportModel, file_shp, airportmodel_mapping,
        transform=True, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
