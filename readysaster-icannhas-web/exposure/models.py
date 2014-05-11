from django.contrib.gis.db import models

from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from model_utils import Choices


# Abstract model class containing geodata for a structure
class Structure(models.Model):
    BUILDING_MATERIAL_CHOICES = Choices(
        ('W', 'wood', _(u'Wood')),
        ('H', 'hybrid', _(u'Makeshift/Hybrid')),
        ('M', 'masonry', _(u'Masonry')),
        ('C', 'concrete', _(u'Concrete')),
        ('S', 'steel', _(u'Steel'))
    )

    STRUCTURAL_TYPE_CHOICES = Choices(
        ('W-1', 'w1', _(u'Wood, light frame')),
        ('W-2', 'w2', _(u'Bamboo')),

        ('H-1', 'h1', _(u'Makeshift')),

        ('M-1', 'm1', _(u'Concrete hollow blocks with wood or light metal')),
        ('M-2', 'm2', _(u'Concrete hollow blocks')),
        ('M-3', 'm3', _(u'Adobe')),
        ('M-4', 'm4', _(u'Unreinforced masonry bearing walls')),

        ('C-1', 'c1', _(u'Reinforced concrete moment frames with wood or light metal')),
        ('C-2', 'c2', _(u'Reinforced concrete moment frames')),
        ('C-3', 'c3', _(u'Concrete shear walls and frames')),
        ('C-4', 'c4', _(u'Precast frame')),

        ('S-1', 's1', _(u'Steel moment frame')),
        ('S-2', 's2', _(u'Light metal frame')),
        ('S-3', 's3', _(u'Steel frame with cast-in-place concrete shear walls')),
    )

    lon = models.FloatField()
    lat = models.FloatField()

    geo = models.PointField(srid=4326)
    objects = models.GeoManager()

    identifier = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/structures')

    # structural description
    # building material
    building_material = models.CharField(
        max_length=1, choices=BUILDING_MATERIAL_CHOICES, default=BUILDING_MATERIAL_CHOICES.wood
    )

    structural_type = models.CharField(
        max_length=3, choices=STRUCTURAL_TYPE_CHOICES, default=STRUCTURAL_TYPE_CHOICES.w1
    )

    n_storeys = models.IntegerField(default=1)

    class Meta:
        abstract = True


class Household(Structure, TimeStampedModel):
    size = models.IntegerField(default=None, null=True, blank=True)

    # for alerts
    contact_number = models.CharField(blank=True, max_length=50)
