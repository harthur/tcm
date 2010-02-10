# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

from tcm.testcases.objects import Testcase
import json

def testcase(request):
    if request.method == "GET":
       error = require(request.GET, ['id'])
       if error:
           return error

       tc = Testcase.get(request.GET)
       return HttpResponse(json.loads(tc))

    elif request.method == "POST":
       dict = json.loads(request.raw_post_data)
       error = require(dict, ['title', 'steps', 'product'])
       if error:
           return error

       id = Testcase.create(dict)
       return HttpResponse(json.dumps({"id" : id}))

#def product(request):
 #   if request.method == "GET":
  #     if 'id' in request.GET:
   #    elif 'name' in request.GET:
    #   else:
           

#def tests(request):


def error(message):
   return HttpResponse(json.dumps({"error": message}))

def require(params, required):
    for field in required:
       if not field in params:
          return error("missing field: " + field)
