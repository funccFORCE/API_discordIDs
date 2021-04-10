from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.shortcuts import redirect

def home(request):
    return HttpResponse("Hello")