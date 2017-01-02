import os
from django.contrib.gis.utils import LayerMapping
from .models import UrbanAreaModel

urbanareasmodel_mapping = {
    'scalerank' : 'scalerank',
    'featurecla' : 'featurecla',
    'area_sqkm' : 'area_sqkm',
    'geom' : 'MULTIPOLYGON',
}


file_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/urban_areas', 'ne_10m_urban_areas.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        UrbanAreaModel, file_shp, urbanareasmodel_mapping,
        transform=True, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
