from django.shortcuts import render
from .models import Faculty, Department, Group, Subject, Teacher, Student

def home(request):
    return render(request, 'home.html')

def faculty(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculties.html', {'faculties': faculties})

def department(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})

def group(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})

def subject(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})

def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def student(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})
