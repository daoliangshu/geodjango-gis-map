import os
from django.contrib.gis.utils import LayerMapping
from .models import AdminBoundaryModel

adminboundarymodel_mapping = {
    'fid_ne_10m' : 'FID_ne_10m',
    'scalerank' : 'scalerank',
    'featurecla' : 'featurecla',
    'note_field' : 'note_',
    'name' : 'name',
    'comment' : 'comment',
    'adm0_usa' : 'adm0_usa',
    'adm0_left' : 'adm0_left',
    'adm0_right' : 'adm0_right',
    'adm0_a3_l' : 'adm0_a3_l',
    'adm0_a3_r' : 'adm0_a3_r',
    'sov_a3_l' : 'sov_a3_l',
    'sov_a3_r' : 'sov_a3_r',
    'type' : 'type',
    'labelrank' : 'labelrank',
    'geom' : 'MULTILINESTRING',
}


file_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/admin_boundary_lines', 'ne_10m_admin_0_boundary_lines_land.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        AdminBoundaryModel, file_shp, adminboundarymodel_mapping,
        transform=True, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
