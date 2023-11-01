from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.urls import reverse
from django.db.models import Q
from .forms import StudentForm

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


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_usn = form.cleaned_data['usn']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email_id = form.cleaned_data['email_id']
            new_placed_company = form.cleaned_data['placed_company']
            new_branch = form.cleaned_data['branch']
            new_cgpa = form.cleaned_data['cgpa']
            new_avatar = form.cleaned_data['avatar']


            new_student = Student(
                usn = new_usn,
                first_name = new_first_name,
                last_name = new_last_name,
                branch = new_branch,
                email_id = new_email_id,
                placed_company = new_placed_company,
                cgpa = new_cgpa,
                avatar  = new_avatar, 
            )
            new_student.save()
            context = {'form':StudentForm(),
                       'success': True}
            return render(request, 'info/addstud.html',context)
    else:
        form = StudentForm()
    context = {'form': StudentForm()}
    return render(request , 'info/addstud.html', context)