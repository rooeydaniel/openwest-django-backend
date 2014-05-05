# -*- coding: utf-8 -*-
from django.db import models

from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Task'
        db.create_table('task_task_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('create_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['task.Category'])),
        ))
        db.send_create_signal(u'task', ['Task'])

        # Adding M2M table for field tags on 'Task'
        m2m_table_name = db.shorten_name('task_task_item_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm[u'task.task'], null=False)),
            ('tag', models.ForeignKey(orm[u'task.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['task_id', 'tag_id'])

        # Adding model 'Category'
        db.create_table(u'task_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'task', ['Category'])

        # Adding model 'Tag'
        db.create_table(u'task_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'task', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Task'
        db.delete_table('task_task_item')

        # Removing M2M table for field tags on 'Task'
        db.delete_table(db.shorten_name('task_task_item_tags'))

        # Deleting model 'Category'
        db.delete_table(u'task_category')

        # Deleting model 'Tag'
        db.delete_table(u'task_tag')


    models = {
        u'task.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'task.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'task.task': {
            'Meta': {'object_name': 'Task', 'db_table': "'task_task_item'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['task.Category']"}),
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['task.Tag']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['task']