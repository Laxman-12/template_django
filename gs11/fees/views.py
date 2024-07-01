from django.shortcuts import render
from django.http import HttpResponse

def fees_django(request):
    return render(request,'fees/feesone.html')

def fees_python(request):
    return render(request,'fees/feestwo.html')
