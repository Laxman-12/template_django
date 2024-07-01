from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    cname= 'Django'
    duration ='4 Month'
    seats= 10
    django_deatials = {'nm':cname, 'du':duration, 'st':seats}

    return render(request,'course/courseone.html',
                  context= django_deatials)                      

def learn_python(request):
    return render(request,'course/coursetwo.html')

