# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Province.region'
        db.add_column(u'rp_province', 'region',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rp.Region'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Province.region'
        db.delete_column(u'rp_province', 'region_id')


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