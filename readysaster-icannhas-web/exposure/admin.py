from django.contrib.gis import admin
from .models import Household


class HouseholdAdmin(admin.OSMGeoAdmin):
    pass


admin.site.register(Household, HouseholdAdmin)
