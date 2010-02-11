import tcm.testcases.couches as couches
import json

testcases = couches.testcases
products = couches.products

class Testcase():
    @staticmethod
    def create(dict):
        doc = json.dumps(dict)
        id = testcases.create(doc)
        return id

    @staticmethod
    def get(dict):
        id = dict['id']
        doc = testcases[id].copy()
        couches.sanitize(doc)
        return doc


class Product():
    @staticmethod
    def create(dict):
        doc = json.dumps(dict)
        id = testcases.create(doc)
        return id

    @staticmethod
    def get(dict):
        if 'id' in dict:
            id = dict['id']
            doc = products[id]
            return couches.sanitize(doc)
       #elif 'name' in dict:
        else:
            return products.view(settings.COUCH_DESIGN + "/by_title")
             
           
