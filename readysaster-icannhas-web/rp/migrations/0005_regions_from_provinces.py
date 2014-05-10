# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

        for province in orm.Province.objects.all():
            region_name = province.region_name
            if region_name == 'ARM':
                region_name = 'ARMM'

            region, created = orm.Region.objects.get_or_create(
                name=region_name,
                description=province.region_desc
            )
            province.region = region
            province.save()

    def backwards(self, orm):
        "Write your backwards methods here."

        for region in orm.Region.objects.all():
            provinces = region.province_set.all()
            for province in provinces:
                province.region_name = region.name
                province.region_desc = region.description
                province.save()

    models = {
        u'rp.municipality': {
            'Meta': {'object_name': 'Municipality'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rp.Province']", 'null': 'True', 'blank': 'True'}),
            'province_name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        u'rp.province': {
            'Meta': {'object_name': 'Province'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rp.Region']", 'null': 'True', 'blank': 'True'}),
            'region_desc': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'region_name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        u'rp.region': {
            'Meta': {'object_name': 'Region'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['rp']
    symmetrical = True
