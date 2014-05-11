# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hazard'
        db.create_table(u'hazard_hazard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal(u'hazard', ['Hazard'])

        # Adding model 'Event'
        db.create_table(u'hazard_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal(u'hazard', ['Event'])

        # Adding M2M table for field associated_hazards on 'Event'
        m2m_table_name = db.shorten_name(u'hazard_event_associated_hazards')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'hazard.event'], null=False)),
            ('hazard', models.ForeignKey(orm[u'hazard.hazard'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'hazard_id'])

        # Adding model 'ReturnPeriod'
        db.create_table(u'hazard_returnperiod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('years', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
        ))
        db.send_create_signal(u'hazard', ['ReturnPeriod'])

        # Adding model 'RainfallReturnPeriodData'
        db.create_table(u'hazard_rainfallreturnperioddata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('municipality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rp.Municipality'])),
            ('return_period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hazard.ReturnPeriod'])),
            ('rainfall_amount', self.gf('django.db.models.fields.FloatField')()),
            ('rainall_duration', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'hazard', ['RainfallReturnPeriodData'])

        # Adding unique constraint on 'RainfallReturnPeriodData', fields ['municipality', 'return_period']
        db.create_unique(u'hazard_rainfallreturnperioddata', ['municipality_id', 'return_period_id'])

        # Adding model 'FloodingWarning'
        db.create_table(u'hazard_floodingwarning', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hazard.Event'])),
            ('numerical_rainfall_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('descriptive_rainfall_amount', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'hazard', ['FloodingWarning'])

        # Adding M2M table for field municipality on 'FloodingWarning'
        m2m_table_name = db.shorten_name(u'hazard_floodingwarning_municipality')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('floodingwarning', models.ForeignKey(orm[u'hazard.floodingwarning'], null=False)),
            ('municipality', models.ForeignKey(orm[u'rp.municipality'], null=False))
        ))
        db.create_unique(m2m_table_name, ['floodingwarning_id', 'municipality_id'])

        # Adding model 'FloodMap'
        db.create_table(u'hazard_floodmap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('municipality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rp.Municipality'])),
            ('return_period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hazard.ReturnPeriod'])),
            ('map_kml', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'hazard', ['FloodMap'])

        # Adding unique constraint on 'FloodMap', fields ['municipality', 'return_period']
        db.create_unique(u'hazard_floodmap', ['municipality_id', 'return_period_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'FloodMap', fields ['municipality', 'return_period']
        db.delete_unique(u'hazard_floodmap', ['municipality_id', 'return_period_id'])

        # Removing unique constraint on 'RainfallReturnPeriodData', fields ['municipality', 'return_period']
        db.delete_unique(u'hazard_rainfallreturnperioddata', ['municipality_id', 'return_period_id'])

        # Deleting model 'Hazard'
        db.delete_table(u'hazard_hazard')

        # Deleting model 'Event'
        db.delete_table(u'hazard_event')

        # Removing M2M table for field associated_hazards on 'Event'
        db.delete_table(db.shorten_name(u'hazard_event_associated_hazards'))

        # Deleting model 'ReturnPeriod'
        db.delete_table(u'hazard_returnperiod')

        # Deleting model 'RainfallReturnPeriodData'
        db.delete_table(u'hazard_rainfallreturnperioddata')

        # Deleting model 'FloodingWarning'
        db.delete_table(u'hazard_floodingwarning')

        # Removing M2M table for field municipality on 'FloodingWarning'
        db.delete_table(db.shorten_name(u'hazard_floodingwarning_municipality'))

        # Deleting model 'FloodMap'
        db.delete_table(u'hazard_floodmap')


    models = {
        u'hazard.event': {
            'Meta': {'object_name': 'Event'},
            'associated_hazards': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['hazard.Hazard']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'hazard.floodingwarning': {
            'Meta': {'object_name': 'FloodingWarning'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'descriptive_rainfall_amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hazard.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'municipality': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['rp.Municipality']", 'symmetrical': 'False'}),
            'numerical_rainfall_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'hazard.floodmap': {
            'Meta': {'unique_together': "(('municipality', 'return_period'),)", 'object_name': 'FloodMap'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map_kml': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'municipality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rp.Municipality']"}),
            'return_period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hazard.ReturnPeriod']"})
        },
        u'hazard.hazard': {
            'Meta': {'object_name': 'Hazard'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'hazard.rainfallreturnperioddata': {
            'Meta': {'unique_together': "(('municipality', 'return_period'),)", 'object_name': 'RainfallReturnPeriodData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rp.Municipality']"}),
            'rainall_duration': ('django.db.models.fields.FloatField', [], {}),
            'rainfall_amount': ('django.db.models.fields.FloatField', [], {}),
            'return_period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hazard.ReturnPeriod']"})
        },
        u'hazard.returnperiod': {
            'Meta': {'object_name': 'ReturnPeriod'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'years': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
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

    complete_apps = ['hazard']