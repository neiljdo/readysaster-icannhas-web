from django.shortcuts import render
from django.views import generic

from .models import FloodingWarning
from .forms import FloodingWarningForm


class FloodingWarningCreateView(generic.CreateView):
    model = FloodingWarning
    form_class = FloodingWarningForm
    template_name = 'hazard/flooding_warning_create.html'

    # def get_success_url(self):
    #     return reverse_lazy('hazard:flood_warning' kwargs={'id': self.object.id })
