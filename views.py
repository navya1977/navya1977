from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("This is my First Page")


def about(request):
    return HttpResponse("This is About Page")


def contact(request):
    return HttpResponse("My Number is: 9533624164")
