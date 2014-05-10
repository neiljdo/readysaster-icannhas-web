# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Household'
        db.create_table(u'exposure_household', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('geo', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('building_material', self.gf('django.db.models.fields.CharField')(default='W', max_length=1)),
            ('structural_type', self.gf('django.db.models.fields.CharField')(default='W-1', max_length=3)),
            ('n_storeys', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('size', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('contact_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'exposure', ['Household'])


    def backwards(self, orm):
        # Deleting model 'Household'
        db.delete_table(u'exposure_household')


    models = {
        u'exposure.household': {
            'Meta': {'object_name': 'Household'},
            'building_material': ('django.db.models.fields.CharField', [], {'default': "'W'", 'max_length': '1'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'geo': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'n_storeys': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'structural_type': ('django.db.models.fields.CharField', [], {'default': "'W-1'", 'max_length': '3'})
        }
    }

    complete_apps = ['exposure']