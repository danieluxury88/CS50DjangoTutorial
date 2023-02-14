from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hola Mundo!")


def daniel(request):
    return HttpResponse("Hola Daniel!")


def joha(request):
    return HttpResponse("Hola Joha!")


def greet(request, name):
    return HttpResponse(f"Hola, {name.capitalize()}!")