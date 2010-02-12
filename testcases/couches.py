from django.conf import settings
from couchdb import Server
from couchdb.design import ViewDefinition

SERVER = Server(settings.COUCH_SERVER)

dbs = {'testcases' : SERVER['testcases'], 'products' : SERVER['products']}

views = {
    'testcases' : [
        ViewDefinition(settings.COUCH_DESIGN, 'by_title',
        """
        function(doc) {
            emit(doc.title, doc);
        }
        """),

        ViewDefinition(settings.COUCH_DESIGN, 'by_collection',
        """
        function(doc) {
            var collections = doc.collections;
            for(var i = 0; i < collections.length; i++)
              emit(doc.collections[i], doc);
        }
        """)
    ],

    'products' : [
        ViewDefinition(settings.COUCH_DESIGN, 'by_name',
        """
        function(doc) {
            emit(doc.name, doc);
        }
        """)
    ]
}

def sanitize(doc):
    del doc['_id']
    del doc['_rev']

