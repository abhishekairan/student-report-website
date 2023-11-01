from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest as Request
from .models import Student, Marks

# Create your views here.

def home(request: Request):
    return render(request, 'index.html',context={'page':'Home'})


def result(request: Request):

    queryset = Student.objects.all()

    return render(request, 'result.html',context={'page':'Result','students':queryset})

def studentReport(request: Request,id: int):
    student= Student.objects.get(id = id)
    queryset = Marks.objects.filter(student_name = student)

    return render(request, 'student-report.html',context={'marks':queryset,'student':student,'page':f''})