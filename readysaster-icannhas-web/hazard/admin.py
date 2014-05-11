from django.contrib import admin

from .models import Hazard, Event, FloodMap

# Register your models here.

admin.site.register(Hazard)
admin.site.register(Event)
admin.site.register(FloodMap)