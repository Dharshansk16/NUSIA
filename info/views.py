from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    context =  {'students':Student.objects.all()}
    return render(request , 'info/home.html', context)



def studentProfile(request ,pk):
    student = Student.objects.get(id=pk)
    context = {'student':student}
    return render(request, 'info/profile.html', context)


