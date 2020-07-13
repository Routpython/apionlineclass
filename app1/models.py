

from django.db import models
class EnrollSubjects(models.Model):
    no=models.IntegerField()
    contact=models.IntegerField()

class AddNewClasses(models.Model):
    no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    faculty=models.CharField(max_length=60)
    date=models.DateField()
    time=models.TimeField()
    price=models.FloatField()
    duration=models.IntegerField()

class StudentModel(models.Model):
    no=models.AutoField(primary_key=True)
    stu_name=models.CharField(max_length=40)
    contact=models.IntegerField(default=None,unique=True)
    email=models.EmailField(default=None,unique=True)
    passw=models.CharField(max_length=40)