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

@login_required(login_url='login')
def update(request , pk):
    if request.method == 'POST':
        student = Student.objects.get(id = pk)
        form = StudentForm(request.POST , request.FILES, instance=student)
        if form.is_valid():
            form.save()
            context = {'form': form,
                       'success':True}
            return render(request , 'info/update.html', context)
    else:
        student = Student.objects.get(id = pk)
        form = StudentForm(instance=student)
    context = {'form':form}
    return render(request , 'info/update.html', context)


@login_required(login_url='login')
def delete(request , pk):
    if request.method == "POST":
        student = Student.objects.get(id = pk)
        student.delete()
        return redirect('home')
    student= Student.objects.get(id =pk)
    return render(request, 'info/delete.html', {'obj':student})


