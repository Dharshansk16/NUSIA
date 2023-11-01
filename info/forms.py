from django import forms
from .models import Student
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields ='__all__'
        labels = {
            'usn': 'USN',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email_id' :'Email ID',
            'branch' : 'Branch',
            'placed_company': 'Placed Company',
            'cgpa':'CGPA',
            'avatar': 'Profile Picture',
        }
        widgets = {
            'usn':forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email_id' :forms.EmailInput(attrs = {'class':'form-control' }),
            'branch' : forms.TextInput(attrs={'class':'form-control'}),
            'placed_company':forms.TextInput(attrs={'class':'form-control'}),
            'cgpa':forms.NumberInput(attrs={'class': 'form-control'}),
            'avatar':forms.FileInput(attrs ={'class': 'form-control'}),
        }