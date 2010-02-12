from django.conf import settings
import tcm.testcases.couches as couches
import json

class Document(object):
    def create(self, dict):
        obj = self.defaults.update(dict)
        doc = json.dumps(obj)
        id = self.db.create(doc)
        return id

    def get(self, dict):
        if 'id' in dict:
            id = dict['id']
            doc = self.db[id]
            return couches.sanitize(doc)
        else:
            return self.db.view(settings.COUCH_DESIGN + "/by_name")


class Testcase(Document):
    db = couches.dbs['testcases']
    defaults = { 
        'automated': False,
        'enabled' : True 
    }

class Product(Document):
    db = couches.dbs['products']
    defaults = { }




# make these classes look static
Testcase = Testcase()
Product = Product()



             
           
