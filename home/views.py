from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_page(request):
    return HttpResponse("Hello My Friend :)))   this is home page!! ")