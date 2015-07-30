# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def migrate_client_data_into_client_object(apps, schema_editor):
    '''
    migrating data from project.client to new Client object
    '''
    Project = apps.get_model("entries", "Project")
    Client = apps.get_model("entries", "Client")
    for project in Project.objects.all():
        client_object, create = Client.get_or_create(name=project.name)
        project.client = client_object
        project.save()

class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20150723_0819'),
    ]

    operations = [
        migrations.RunPython(migrate_client_data_into_client_object),
    ]
