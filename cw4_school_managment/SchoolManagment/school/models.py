from django.db import models

GENDER = [("F", "FEMALE"), ("M", "MALE")]


class Student(models.Model):
    name = models.CharField("name of the student", max_length=100, required=True)
    roll_number = models.CharField("roll of the student", max_length=10,unique=True, required=True)
    date_of_birth = models.DateField("birthdate of the student", required=True)
    gender = models.CharField("gender of the student", choices=GENDER)
    address=models.TextField("the address of the student",required=True)
    email=models.EmailField("email address of the student",required=True,unique=True)
    # teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)


class Teacher(models.Model):
    name=models.CharField("name of the teacher",required=True,max_length=100)
    subject=models.CharField("the subject taught by the teacher",required=True,max_length=100)
    date_of_birth=models.DateField("birthdate of the teacher",required=True)
    gender=models.CharField("gender of the teacher",choices=GENDER,required=True)
    address=models.TextField("address of the teacher",required=True)
    email=models.EmailField("email address of the teacher",required=True,unique=True)




class Subject(models.Model):
    ...


class Exam(models.Model):
    ...


class Result(models.Model):
    ...


class Attendance(models.Model):
    ...


class Assignment(models.Model):
    ...


class Notice(models.Model):
    ...


class LibraryBook(models.Model):
    ...
