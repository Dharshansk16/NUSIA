from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Student(models.Model):
    usn = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(null=True , max_length=100)
    branch = models.CharField(max_length=50)
    placed_company = models.CharField(max_length=100)
    cgpa = models.FloatField()
    avatar = models.ImageField(upload_to="static/images",null=True, default="static/images/avatar.svg", blank=True)
    updated = models.DateTimeField(auto_now=True) # Takes time stamp every time a user submits or saves.
    created = models.DateTimeField(auto_now_add=True) #Takes time stamp when we first submit or save(created time).


    def clean(self):
        usn_upper = self.usn.upper()
        if not usn_upper.startswith("NNM"):
            raise ValidationError({'usn': "USN must start with 'NNM'."})
        self.usn = usn_upper
        
        if self.cgpa < 0 or self.cgpa>10:
            raise ValidationError({'cgpa':"Invalid value"})
    
    def save(self, *args, **kwargs):
        self.full_clean()

        # Normalize placed_company and branch
        if self.placed_company:
            self.placed_company = self.placed_company.strip().upper()
        if self.branch:
            self.branch = self.branch.strip().upper()

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return f'Student: {self.usn} {self.first_name} {self.last_name}'


class Certification(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name="certifications")
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    certificate_id = models.CharField(max_length=100, unique=True)
    certificate_link = models.URLField(null=True, blank=True)
    certificate_file = models.FileField(upload_to="static/certifications", null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.student.first_name}'

    class Meta:
        ordering = ['-issue_date']
    