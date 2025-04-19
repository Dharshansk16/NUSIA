from info.models import Student, Certification
from django.db.models import Count, Q
from django.db import connection


def run():
    # company_data = Student.objects.values('placed_company').annotate(count=Count('id')).order_by('-count')
    # print(company_data)
    # q="nnm"
    # students = Student.objects.filter(
    #     Q(usn__icontains=q) |
    #     Q(placed_company__icontains=q) |
    #     Q(branch__icontains=q) |
    #     Q(cgpa__icontains = q) |
    #     Q(first_name__icontains = q) |
    #     Q(last_name__icontains = q)
    # )
    # print(students)
    # print(connection.queries)
    pass