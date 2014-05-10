import os
from django.contrib.gis.utils import LayerMapping
from .models import Province, Municipality


DIR_PATH = os.path.dirname(__file__)


# shapefiles
province_shp = os.path.join(DIR_PATH, '../../data/NAMRIA/NAMRIA - Open Data/NAMRIA/Admin Boundaries/Philadmin2009_Prov_gcswgs84.shp')
province_shp = os.path.abspath(province_shp)

municipality_shp = os.path.join(DIR_PATH, '../../data/NAMRIA/NAMRIA - Open Data/NAMRIA/Admin Boundaries/Philadmin2009_Municipal_gcswgs84.shp')
municipality_shp = os.path.abspath(municipality_shp)


province_mapping = {
    'name' : 'PROVINCE',
    'region_name': 'REGION',
    'region_desc': 'REG_DESC',
    'geom' : 'MULTIPOLYGON',
}

municipality_mapping = {
    'name' : 'MUNICIPALI',
    'province_name': 'PROVINCE',
    'geom' : 'MULTIPOLYGON',
}


def run(verbose=True):
    # import provinces
    lm = LayerMapping(Province, province_shp, province_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

    # import municipalities
    lm = LayerMapping(Municipality, municipality_shp, municipality_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
