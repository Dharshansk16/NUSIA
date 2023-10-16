from django.shortcuts import render
from .models import Student
from django.db.models import Q

# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    students = Student.objects.filter(
        Q(usn__icontains=q) |
        Q(placed_company__icontains=q) |
        Q(branch__icontains=q) |
        Q(cgpa__icontains = q) |
        Q(first_name__icontains = q) |
        Q(last_name__icontains = q)
    )
    context =  {'students':students}
    return render(request , 'info/home.html', context)


def studentProfile(request ,pk):
    studentId = Student.objects.get(id=pk)
    context = {'studentId':studentId}
    return render(request, 'info/profile.html', context)


