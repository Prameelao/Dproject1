from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1>Hardik pandya is captain of MI</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>Mahel is vicecaptain of MI</h1>')