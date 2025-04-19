from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import Student , Certification
from django.urls import reverse
from django.db.models import Q,Count
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
import json
# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    #Checks whether user exits else throws error message
    if request.method=="POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request , 'user does not exist')
        #authenticate checks for username and pass if it exits in the db if true, then sets the user
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('home')
        else:
            messages.error(request , "Username or Password does not exist")

    context = {'page':page}
    return render(request , 'info/loginpage.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    sort= request.GET.get('sort')
    students = Student.objects.filter(
        Q(usn__icontains=q) |
        Q(placed_company__icontains=q) |
        Q(branch__icontains=q) |
        Q(cgpa__icontains = q) |
        Q(first_name__icontains = q) |
        Q(last_name__icontains = q)
    )
    if sort=="cgpa":
        students=students.order_by("-cgpa")
    elif sort=="recent":
        students=students.order_by('-created')
    else:
        students=students.order_by('created')
    context =  {'students':students, 'sort':sort}
    return render(request , 'info/home.html', context)

def studentProfile(request ,pk):
    studentId = Student.objects.get(id=pk)
    context = {'studentId':studentId}
    return render(request, 'info/profile.html', context)


def analyticsView(request):
    #Company vs Student Count
    company_count = Student.objects.values('placed_company').annotate(count=Count('id')).order_by('-count')
    company_labels = [item['placed_company'] for item in company_count]
    company_data = [item['count'] for item in company_count]

    #Branch vs Student Count
    branch_count = Student.objects.values('branch').annotate(count=Count('id')).order_by('-count')
    branch_labels = [item['branch'] for item in branch_count]
    branch_data = [item['count'] for item in branch_count]

    

    context = {
        "company_labels": json.dumps(company_labels),
        "company_data": json.dumps(company_data),
        "branch_labels": json.dumps(branch_labels),
        "branch_data": json.dumps(branch_data),
    }
    return render(request, "info/analytics.html", context)


@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                student = form.save(commit=False) 
                student.full_clean()
                student.save()
                return render(request, "info/addstud.html", {'form':StudentForm(), "success":True})
            except Exception as e:
                 for field, errors in e.message_dict.items():
                    for error in errors:
                        form.add_error(field, error)
    else:
        form = StudentForm()
    context = {'form': StudentForm()}
    return render(request , 'info/addstud.html', context)

@login_required(login_url='login')
def update(request , pk):
    if request.method == 'POST':
        student = Student.objects.get(id = pk)
        form = StudentForm(request.POST , request.FILES, instance=student)
        if form.is_valid():
            try:
                form.save()
                context= {'form': form,'student':student,
                          'success':True}
                return render(request, "info/update.html", context)
            except ValidationError as e:
                for field, error in e.message_dict.items():
                    form.add_error(field,error)
    else:
        student = Student.objects.get(id = pk)
        form = StudentForm(instance=student)
    context = {'form':form , "student":student}
    return render(request , 'info/update.html', context)


@login_required(login_url='login')
def delete(request , pk):
    if request.method == "POST":
        student = Student.objects.get(id = pk)
        student.delete()
        return redirect('home')
    student= Student.objects.get(id =pk)
    return render(request, 'info/delete.html', {'obj':student})


