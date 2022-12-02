from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 style=\"color:blue\"> Hello, world!</h1>")
def greet(request, name):
    return HttpResponse(f"Hello, {name}!")
def ko(request, name):
    return HttpResponse(f"Hello, ko!")