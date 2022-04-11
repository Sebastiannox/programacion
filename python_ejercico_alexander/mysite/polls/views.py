from django.shortcuts import render
from django.db import connections


# Create your views here.
from django.http import HttpResponse


def index(request):
    c=connections['']
    return HttpResponse("Hello, world. You're at the polls index.")
