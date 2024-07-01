from django.shortcuts import render
from django .http import HttpResponse
# Create your views here.
def learn_django(request):
    return HttpResponse('<h1>hellow Django</h1>')

def learn_python(request):
    return HttpResponse('<h1>hellow python</h1>')

def learn_var(request):
    a='<h1>hellow variable</h1>'
    return HttpResponse(a)

def learn_math(request):
    a=10+10
    return HttpResponse(a)

def learn_format(request):
    a= 'GeekyShows'
    return HttpResponse(f'Hellow How are You{a}')

