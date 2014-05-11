from django.contrib import admin

from .models import Hazard, Event, FloodMap, FloodingWarning, RainfallReturnPeriodData, ReturnPeriod

# Register your models here.

admin.site.register(Hazard)
admin.site.register(Event)
admin.site.register(FloodMap)
admin.site.register(FloodingWarning)
admin.site.register(ReturnPeriod)
admin.site.register(RainfallReturnPeriodData)