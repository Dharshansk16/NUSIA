# Generated by Django 5.1.7 on 2025-03-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_alter_student_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='usn',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
