from factory import Faker, SubFactory, LazyAttribute
from factory.django import DjangoModelFactory
from faker.providers import person, misc, date_time, lorem, python

from .models import Student, Address, Teacher, Subject, Exam, Notice, Assignment, LibraryBook, Attendance, Class, \
    Result, ATTENDANCE_STATUS


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

    name = Faker('sentence', nb_words=4, variable_nb_words=True, ext_word_list=None, provider=lorem)
    date = Faker('date_between_dates', date_start='-30d', end_date='+30d', provider=date_time)
    exam_class = SubFactory(lambda: ClassFactory())


class ResultFactory(DjangoModelFactory):
    class Meta:
        model = Result

    exam = SubFactory(lambda: ExamFactory())
    student = SubFactory(lambda: StudentFactory())
    marks = Faker('pyfloat', left_digits=2, right_digits=2, positive=True, min_value=0, max_value=100, provider=python)


class AttendanceFactory(DjangoModelFactory):
    class Meta:
        model = Attendance

    date = Faker('date_between_dates', date_start='-30d', end_date='+30d', provider=date_time)
    student = SubFactory(lambda: StudentFactory())
    status = Faker('random_element', elements=[choice[0] for choice in ATTENDANCE_STATUS], provider=misc)


class AssignmentFactory(DjangoModelFactory):
    class Meta:
        model = Assignment

    title = Faker('name')
    description = Faker('paragraph', nb_sentences=3, variable_nb_sentences=True, ext_word_list=None, provider=lorem)
    due_date = Faker('date_between_dates', date_start='-30d', end_date='+30d', provider=date_time)
    subject = SubFactory(lambda: SubjectFactory())


class NoticeFactory(DjangoModelFactory):
    class Meta:
        model = Notice

    title = Faker('name')
    description = Faker('paragraph', nb_sentences=3, variable_nb_sentences=True, ext_word_list=None, provider=lorem)
    date = Faker('date_between_dates', date_start='-30d', end_date='+30d', provider=date_time)


class LibraryBookFactory(DjangoModelFactory):
    class Meta:
        model = LibraryBook

    title = Faker('name')
    author = Faker('first_name')
    publication_date = Faker('date_between_dates', date_start='-30d', end_date='+30d', provider=date_time)
    availability_status = Faker('pybool', chance_of_getting_true=50, provider=python)