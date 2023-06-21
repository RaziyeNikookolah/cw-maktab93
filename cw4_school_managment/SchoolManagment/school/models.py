from django.db import models

GENDER = [("F", "FEMALE"), ("M", "MALE")]
ATTENDANCE_STATUS = [("PRESENT", "present"), ("ABSENT", "absent")]


class Student(models.Model):
    name = models.CharField("name of the student", max_length=100, required=True)
    roll_number = models.CharField("roll of the student", max_length=10, unique=True, required=True)
    date_of_birth = models.DateField("birthdate of the student", required=True)
    gender = models.CharField("gender of the student", choices=GENDER)
    address = models.TextField("the address of the student", required=True)
    email = models.EmailField("email address of the student", required=True, unique=True)
    # teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)


class Teacher(models.Model):
    name = models.CharField("name of the teacher", required=True, max_length=100)
    subject = models.CharField("the subject taught by the teacher", required=True, max_length=100)
    date_of_birth = models.DateField("birthdate of the teacher", required=True)
    gender = models.CharField("gender of the teacher", choices=GENDER, required=True)
    address = models.TextField("address of the teacher", required=True)
    email = models.EmailField("email address of the teacher", required=True, unique=True)


class Class(models.Model):
    name = models.CharField("name of the class(e.g.,\"Grade 10\")", required=True, max_length=100)
    section = models.CharField("section of the class(e.g.,\"A\", \"B\")", required=True)
    start_time = models.TimeField("start time of the class", required=True)
    end_time = models.TimeField("end time of the class", required=True)


class Subject(models.Model):
    name = models.CharField("name of the subject", required=True, max_length=100)
    code = models.CharField("unique code for the subject", required=True, max_length=10)


class Exam(models.Model):
    name = models.CharField("name of the exam", required=True, max_length=100)
    date = models.DateField("date of the exam", required=True)
    exam_class = models.ForeignKey(Class, on_delete=models.CASCADE, required=True)


class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, required=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, required=True)
    marks = models.IntegerField("marks obtained by the student")


class Attendance(models.Model):
    date = models.DateField("date for whitch the attendance is recorded", required=True)
    student = models.ForeignKey(Student, "student whose attendance is recorded", on_delete=models.CASCADE())
    status = models.CharField("attendance status", choices=ATTENDANCE_STATUS)


class Assignment(models.Model):
    title=models.CharField("title of the assignment",required=True,max_length=100)
    description=models.TextField("description/instructions for the assignment",required=True)
    due_date=models.DateField("due date for the assignment",required=True)
    subject=models.ForeignKey(Subject,"subject for which the assignment is given",required=True)


class Notice(models.Model):
    ...


class LibraryBook(models.Model):
    ...
