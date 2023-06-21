from django.db import models

GENDER = [("F", "FEMALE"), ("M", "MALE")]
ATTENDANCE_STATUS = [("PRESENT", "present"), ("ABSENT", "absent")]


class Student(models.Model):
    name = models.CharField("name of the student", max_length=100)
    roll_number = models.CharField("roll of the student", max_length=10, unique=True)
    date_of_birth = models.DateField("birthdate of the student")
    gender = models.CharField("gender of the student", choices=GENDER,max_length=10)
    address = models.TextField("the address of the student")
    email = models.EmailField("email address of the student",  unique=True)
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, related_name="students")
    _class=models.OneToOneField("Class",on_delete=models.CASCADE)
    # _class = models.ForeignKey("Class", on_delete=models.CASCADE, related_name="student", unique=True)

    def __str__(self):
        return f'{self.name} {self.roll_number}'


class Address(models.Model):
    street = models.CharField("street", max_length=50)
    city = models.CharField("city", max_length=50)
    state = models.CharField("state", max_length=50)
    zip_code = models.CharField("zip code", max_length=10)
    country = models.CharField("country", max_length=50)

    def __str__(self):
        return f'{self.city}'


class Teacher(models.Model):
    name = models.CharField("name of the teacher", max_length=100)
    # subject = models.CharField("the subject taught by the teacher", required=True, max_length=100)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, related_name="teachers")
    date_of_birth = models.DateField("birthdate of the teacher")
    gender = models.CharField("gender of the teacher", choices=GENDER,max_length=10)
    address = models.TextField("address of the teacher")
    email = models.EmailField("email address of the teacher", unique=True)

    def __str__(self):
        return f'{self.name} {self.subject}'


class Class(models.Model):
    name = models.CharField("name of the class(e.g.,\"Grade 10\")", max_length=100)
    section = models.CharField("section of the class(e.g.,\"A\", \"B\")",max_length=100)
    start_time = models.TimeField("start time of the class")
    end_time = models.TimeField("end time of the class")
    teacher = models.OneToOneField(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Subject(models.Model):
    name = models.CharField("name of the subject",  max_length=100)
    code = models.CharField("unique code for the subject", max_length=10)

    def __str__(self):
        return f'{self.name}'


class Exam(models.Model):
    name = models.CharField("name of the exam",  max_length=100)
    date = models.DateField("date of the exam", )
    exam_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.IntegerField("marks obtained by the student")  # should not be list?

    def __str__(self):
        return f'{self.marks}'


class Attendance(models.Model):
    date = models.DateField("date for whitch the attendance is recorded")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField("attendance status", choices=ATTENDANCE_STATUS,max_length=10)

    def __str__(self):
        return f'{self.status}'


class Assignment(models.Model):
    title = models.CharField("title of the assignment", max_length=100)
    description = models.TextField("description/instructions for the assignment")
    due_date = models.DateField("due date for the assignment")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Notice(models.Model):
    title = models.CharField("title of the notice",  max_length=100)
    description = models.TextField("description/details of the notice")
    date = models.DateField("date on which the notice is posted")

    def __str__(self):
        return f'{self.title}'


class LibraryBook(models.Model):
    title = models.CharField("title of the book",  max_length=100)
    author = models.CharField("author of the book",  max_length=100)
    publication_date = models.DateField(" publication date of the book")
    availability_status = models.BooleanField("availability status of the book")

    def __str__(self):
        return f'{self.title}'
