from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import Student
from django.urls import reverse
from django.db.models import Q
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

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


