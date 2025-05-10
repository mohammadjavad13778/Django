from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse("Hello, welcome Django")
