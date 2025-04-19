from info.models import Student, Certification


def run():
    studentId= Student.objects.get(id=1)
    for c in studentId.certifications.all():
        print(c.title)