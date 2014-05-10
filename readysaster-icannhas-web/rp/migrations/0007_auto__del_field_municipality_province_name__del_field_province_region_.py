# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Municipality.province_name'
        db.delete_column(u'rp_municipality', 'province_name')

        # Deleting field 'Province.region_name'
        db.delete_column(u'rp_province', 'region_name')

        # Deleting field 'Province.region_desc'
        db.delete_column(u'rp_province', 'region_desc')


    def backwards(self, orm):
        # Adding field 'Municipality.province_name'
        db.add_column(u'rp_municipality', 'province_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=254),
                      keep_default=False)

        # Adding field 'Province.region_name'
        db.add_column(u'rp_province', 'region_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=254),
                      keep_default=False)

        # Adding field 'Province.region_desc'
        db.add_column(u'rp_province', 'region_desc',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=254),
                      keep_default=False)


    models = {
        u'rp.municipality': {
            'Meta': {'object_name': 'Municipality'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rp.Province']", 'null': 'True', 'blank': 'True'})
        },
        u'rp.province': {
            'Meta': {'object_name': 'Province'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rp.Region']", 'null': 'True', 'blank': 'True'})
        },
        u'rp.region': {
            'Meta': {'object_name': 'Region'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['rp']