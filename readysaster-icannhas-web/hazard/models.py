from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from core.constants import CHOICES


HAZARD_CHOICES = CHOICES['HAZARD']
EVENT_CHOICES = CHOICES['EVENT']
RAINFALL_WARNING_CHOICES = CHOICES['RAINFALL_WARNING']


class Hazard(models.Model):
    label = models.IntegerField(choices=HAZARD_CHOICES, unique=True)


class Event(models.Model):
    label = models.IntegerField(choices=EVENT_CHOICES, unique=True)
    associated_hazards = models.ManyToManyField('Hazard')

    '''
    sample event-hazard associations:

    Event: [Hazards]

    Rainfall: [Flooding, Landslides]
    Typhoon: [Flooding, Severe Wind, Storm Surge]
    Earthquake: [Ground Shaking, Liquefaction, Tsunami]
    '''


class ReturnPeriod(models.Model):
    years = models.PositiveIntegerField(unique=True)

    def __unicode__(self):
        return self.years 

class RainfallReturnPeriodData(models.Model):
    municipality = models.ForeignKey('rp.Municipality')

    return_period = models.ForeignKey(ReturnPeriod)

    rainfall_amount = models.FloatField(
        help_text=_(u'Amount of rainfall in milimeters'))
    rainall_duration = models.FloatField(
        help_text=_(u'Number of hours for which the specified amount fell')
    )

    class Meta:
        unique_together = (('municipality', 'return_period'),)


class FloodingWarning(TimeStampedModel):
    event = models.ForeignKey(Event)
    municipality = models.ManyToManyField('rp.Municipality')

    numerical_rainfall_amount = models.FloatField(
        _(u'Rainfall amount in milimeters per hour'),
        null=True,
        blank=True)
    descriptive_rainfall_amount = models.IntegerField(
        choices=RAINFALL_WARNING_CHOICES,
        default=RAINFALL_WARNING_CHOICES.none
    )

    def save(self, *args, **kwargs):
        if not self.numerical_rainfall_amount and not self.descriptive_rainfall_amount:
            raise Exception('At least one of the rainfall fields must be supplied')
        #TODO: Populate descriptive rainfall field if numerical was supplied
        return super(FloodingWarning, self).save(*args, **kwargs)


class FloodMap(models.Model):
    municipality = models.ForeignKey('rp.Municipality')
    return_period = models.ForeignKey(ReturnPeriod)

    map_kml = models.FileField(
        upload_to='uploads/floodmaps',
    )

    class Meta:
        unique_together = (('municipality', 'return_period'),)

    def __unicode__(self):
        return '{0}: {1}'.format(self.municipality, self.return_period)
