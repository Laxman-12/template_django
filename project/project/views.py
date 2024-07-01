from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    data={
        'title':'Home new',
        'bdata':'welcome to my project',
        'clist':['php','java','Django'],
        'numbers':[10,15,25,34,17,18],
        'student_detail':[
            {'name':'ram','roll':105},
            {'name':'shyam','roll':102},
        ]
    }
    return render (request,"index.html",data)


def aboutUs(request):
    return HttpResponse("welcome to my project")
def course(request):
    return HttpResponse("welcome to my course")

def courseDetails(request,courseid):
    return HttpResponse(courseid)