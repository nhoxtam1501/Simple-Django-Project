from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    return HttpResponse("Hello World with ku ")


def hello(response):
    return HttpResponse("Hello, Welcome back")
