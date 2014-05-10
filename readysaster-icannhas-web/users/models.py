# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return self.username


# User profiles
class LGU(TimeStampedModel):
    user = models.OneToOneField('User')
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True)

    municipality = models.ForeignKey('rp.Municipality')

    def __unicode__(self):
        return self.name
