from factory import Faker, SubFactory, LazyAttribute
from factory.django import DjangoModelFactory
from faker.providers import person, misc, date_time, lorem

from .models import Student, Address, Teacher, Subject, Exam, Notice, Assignment, LibraryBook, Attendance, Class, Result


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    name = Faker('first_name')
    roll_number = '22'
    date_of_birth = Faker('date_of_birth', minimum_age=18, maximum_age=65, provider=person)
    gender = Faker('random_element', elements=["F", "M"], provider=misc)
    address = SubFactory(lambda: AddressFactory())
    email = LazyAttribute(lambda o: '%s@example.com' % o.name)
    teacher = SubFactory(lambda: TeacherFactory())
    _class = SubFactory(lambda: ClassFactory())


class AddressFactory(DjangoModelFactory):
    class Meta:
        model = Address

    street = Faker('street_address')
    city = Faker('city')
    state = Faker('state_abbr')
    zip_code = Faker('zip_code')
    country = Faker('country')


class TeacherFactory(DjangoModelFactory):
    class Meta:
        model = Teacher

    name = Faker('first_name')
    # subject = models.CharField("the subject taught by the teacher", required=True, max_length=100)
    subject = SubFactory(lambda: SubjectFactory())
    date_of_birth = Faker('date_of_birth', minimum_age=18, maximum_age=65, provider=person)
    gender = Faker('random_element', elements=["F", "M"], provider=misc)
    address = SubFactory(lambda: AddressFactory())
    email = LazyAttribute(lambda o: '%s@example.com' % o.name)


class SubjectFactory(DjangoModelFactory):
    class Meta:
        model = Subject


class ClassFactory(DjangoModelFactory):
    class Meta:
        model = Class
    name = Faker('sentence', nb_words=3, variable_nb_words=True, ext_word_list=None, provider=lorem)
    section = Faker('random_element', elements=["A", "B"], provider=misc)
    start_time = Faker('time_object', start_datetime=None, end_datetime=None, tzinfo=None, provider=date_time)
    end_time = Faker('time_object', start_datetime=start_time, end_datetime=None, tzinfo=None, provider=date_time)
    teacher = SubFactory(lambda: TeacherFactory())


class ExamFactory(DjangoModelFactory):
    class Meta:
        model = Exam


class ResultFactory(DjangoModelFactory):
    class Meta:
        model = Result


class AttendanceFactory(DjangoModelFactory):
    class Meta:
        model = Attendance


class AssignmentFactory(DjangoModelFactory):
    class Meta:
        model = Assignment


class NoticeFactory(DjangoModelFactory):
    class Meta:
        model = Notice


class LibraryBookFactory(DjangoModelFactory):
    class Meta:
        model = LibraryBook
