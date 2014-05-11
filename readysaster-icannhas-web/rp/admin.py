from django.contrib.gis import admin
from .models import Municipality, Province, Region


class MunicipalityAdmin(admin.OSMGeoAdmin):
    list_display = ['__unicode__', 'province']
    search_fields = ['name']


class ProvinceAdmin(admin.OSMGeoAdmin):
    search_fields = ['name']


class RegionAdmin(admin.OSMGeoAdmin):
    search_fields = ['name']


admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(Region, RegionAdmin)
