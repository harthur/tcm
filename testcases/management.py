from django.db.models import signals
from couchdb.design import ViewDefinition
from django.conf import settings

from couchdb import Server
from couchdb import ResourceNotFound
from couchdb.design import ViewDefinition

import tcm.testcases.couches as couches
import tcm.testcases.models as models

SERVER = Server(settings.COUCH_SERVER)

def createViews(app, created_models, verbosity, **kwargs):
    for dbName in couches.views:
         ViewDefinition.sync_many(couches.dbs[dbName], couches.views[dbName])

def createCouches(app, created_models, verbosity, **kwargs):
    for dbName in couches.dbs:
        try:
            SERVER[dbName]
        except ResourceNotFound:
            SERVER.create(dbName)

# create couchdb views and dbs when 'manage.py syncdb' is called
signals.post_syncdb.connect(createCouches, sender=models)
signals.post_syncdb.connect(createViews, sender=models)
