from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h2>Hello Django I new on django</h2>')


