from django.contrib.gis import admin
from .models import Municipality, Province, Region


admin.site.register(Municipality, admin.OSMGeoAdmin)
admin.site.register(Province, admin.OSMGeoAdmin)
admin.site.register(Region, admin.ModelAdmin)
