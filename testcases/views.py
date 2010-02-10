# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

import tcm.testcases.couches as couches
import json

testcases = couches.testcases

def create(request):
    if request.method == "GET":
       return render_to_response('testcases/create.html')

#def testcase(request):

#def tests(request):
   # no request.GET['collection'] or ['tags'] = product view
   # no request.GET['collection'] = all tags for product
   # one request.GET['collection'] no request.GET['tags'] = all tags in collection
   # one request.GET['tags'] = the running view
   # multiple request.GET['tags'] = specified tags in collection

#def reviews(request):

#def review(request):
