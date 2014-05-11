import json
import urllib
import urllib2

from django.core.files import File
from django.conf import settings

from .models import FloodMap, ReturnPeriod
from rp.models import Municipality


def get_geoserver_baseurl():
    '''
    Just input the layer name, height, width and boundarybox
    '''
    url = settings.NOAH_GEOSERVER_URL + '?'
    url += urllib.urlencode({
        'request': 'GetMap',
        'service': 'WMS',
        'version': '1.1.1',
        'srs': 'EPSG:4326',
        'format': 'kml',
    })
    return url


def get_floodmap_kml_file(layers, bbox, height=720, width=330, styles=''):
    url = get_geoserver_baseurl() + '&' + urllib.urlencode({
        'layers': layers,
        'styles': styles,
        'height': height,
        'width': width,
        'bbox': bbox,
    })
    data = urllib2.urlopen(url)
    data = data.read()
    with open('uploads/floodmaps/map.kml', 'w') as f:
        mapfile = File(f)
        mapfile.write(data)
    return mapfile


def create_floodmap_instances():
    url = settings.NOAH_API_URL + 'flood_maps'
    data = urllib2.urlopen(url)
    data = data.read()
    events = json.loads(data)
    events = events[0]
    for event in events:
        return_period = event['verbose_name']

        # Assuming that NOAH API uses 'N-Years' format in its verbose names
        return_period = int(return_period.split('-')[0])

        floodmaps = event['floods']
        for floodmap in floodmaps:
            centroid = floodmap['center']
            layer = floodmap['geoserver_layer']
            municipality = Municipality.get_instance(lat=centroid['lat'], lng=centroid['lng'])
            return_period = ReturnPeriod.objects.get(return_period=return_period, municipality=municipality)
            coords = municipality.geom.extent
            bbox = ''
            for coord in coords:
                bbox += (coord + ',')
            bbox = bbox[:-1]
            map_kml = municipality.get_floodmap_kml_file(layer, bbox)

    fm = FloodMap(municipality=municipality, return_period=return_period, map_kml=map_kml)
    fm.save()
