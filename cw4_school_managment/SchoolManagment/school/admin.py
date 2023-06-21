from django.contrib import admin

# Register your models here.
from .models import Student,Subject,Address,Attendance,Assignment,Class,Exam
from .models import Result,Notice,Teacher,LibraryBook

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Address)
admin.site.register(Attendance)
admin.site.register(Assignment)
admin.site.register(Class)
admin.site.register(Exam)
admin.site.register(Result)
admin.site.register(Notice)
admin.site.register(Teacher)
admin.site.register(LibraryBook)
