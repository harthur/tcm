from django.db.models import signals
from couchdb.design import ViewDefinition

import tcm.testcases.couches as couches
import tcm.testcases.models as models


# sync couchdb views when 'manage.py syncdb' is called
def createViews(app, created_models, verbosity, **kwargs):
    for dbName in couches.views:
         ViewDefinition.sync_many(couches.dbs[dbName], couches.views[dbName])

signals.post_syncdb.connect(createViews, sender=models)
