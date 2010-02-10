from django.conf import settings
from couchdb import Server
from couchdb import ResourceNotFound
from couchdb.design import ViewDefinition

SERVER = Server(settings.COUCH_SERVER)

def sanitize(doc):
    del doc['_id']
    del doc['_rev']

def db(dbName):
    try:
        SERVER[dbName]
    except ResourceNotFound:
        SERVER.create(dbName)
    return SERVER[dbName]

testcases = db('testcases')
products = db('products')

dbs = {'testcases' : testcases, 'products' : products}

views = {
    'testcases' : [
        ViewDefinition(settings.COUCH_DESIGN, 'by_title',
        """
        function(doc) {
            emit(doc.title, null);
        }
        """)
    ]
}
