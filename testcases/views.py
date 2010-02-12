# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from tcm.testcases.objects import Product

def create(request):
    if request.method == "GET":
       products = Product.get({})
       return render_to_response('testcases/create.html', {'products' : products})

#def testcase(request):

#def tests(request):
   # no request.GET['collection'] or ['tags'] = product view
   # no request.GET['collection'] = all tags for product
   # one request.GET['collection'] no request.GET['tags'] = all tags in collection
   # one request.GET['tags'] = the running view
   # multiple request.GET['tags'] = specified tags in collection

#def reviews(request):

#def review(request):
