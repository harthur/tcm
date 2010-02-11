from django.conf import settings
from couchdb import Server
from couchdb.design import ViewDefinition

SERVER = Server(settings.COUCH_SERVER)

testcases = SERVER['testcases']
products = SERVER['products']

dbs = {'testcases' : testcases, 'products' : products}

views = {
    'testcases' : [
        ViewDefinition(settings.COUCH_DESIGN, 'by_title',
        """
        function(doc) {
            emit(doc.title, null);
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

