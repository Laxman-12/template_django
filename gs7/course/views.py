from django.shortcuts import render
from django.http import HttpResponse
def learn_django(request):
    return HttpResponse('hello django')

def learn_python(request):
    return HttpResponse('Hello python')

# Create your views here.
