from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1>Virat kohli is the captain of RCB</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>Faf Du is vice captain of RCB</h1>')
