from factory import Faker, SubFactory, LazyAttribute
from factory.django import DjangoModelFactory
from faker.providers import person, misc, date_time, lorem, python
import factory.fuzzy
from .models import Student, Address, Teacher, Subject, Exam, Notice, Assignment, LibraryBook, Attendance, Class, \
    Result


class AddressFactory(DjangoModelFactory):
    class Meta:
        model = Address

    street = Faker('street_address')
    city = Faker('city')
    state = Faker('state_abbr')
    # zip_code = Faker('postal_code')
    country = Faker('country')


class SubjectFactory(DjangoModelFactory):
    class Meta:
        model = Subject
    name = Faker('first_name')
    # code = Faker('postal_code')


class TeacherFactory(DjangoModelFactory):
    class Meta:
        model = Teacher

    name = Faker('first_name')
    subject = SubFactory(SubjectFactory)
    date_of_birth = Faker('date_of_birth')
    gender = "M"
    address = SubFactory(AddressFactory)
    email = factory.Sequence(lambda n: 'c_%d@test.com' % n)


class ClassFactory(DjangoModelFactory):
    class Meta:
        model = Class

    name = factory.fuzzy.FuzzyChoice(
        choices=["one", "two", "three", "four", "five"])
    section = Faker('random_element', elements=["A", "B"])
    start_time = Faker('time_object')
    end_time = Faker('time_object')
    teacher = SubFactory(TeacherFactory)


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    name = Faker('first_name')
    roll_number = factory.Sequence(lambda n: "roll%d" % n)
    date_of_birth = Faker('date_of_birth')
    gender = "F"
    address = SubFactory(AddressFactory)
    email = LazyAttribute(lambda o: '%s_%s@example.com' %
                          (o.name, o.roll_number))
    # email = factory.Sequence(lambda n, o: '%s_%d@example.com' % (o.name, n))
    teacher = SubFactory(TeacherFactory)
    student_class = SubFactory(ClassFactory)


class ExamFactory(DjangoModelFactory):
    class Meta:
        model = Exam

    name = factory.fuzzy.FuzzyChoice(
        choices=["math", "science", "art", "religen", "sport"])
    date = Faker('date_between_dates')
    exam_class = SubFactory(ClassFactory)


class ResultFactory(DjangoModelFactory):
    class Meta:
        model = Result

    exam = SubFactory(ExamFactory)
    student = SubFactory(StudentFactory)
    marks = factory.fuzzy.FuzzyChoice(
        choices=[100, 20, 30, 40, 50])


class AttendanceFactory(DjangoModelFactory):
    class Meta:
        model = Attendance

    date = Faker('date_object')
    student = SubFactory(StudentFactory)
    status = factory.fuzzy.FuzzyChoice(
        choices=["PRESENT", "ABSENT"])


class AssignmentFactory(DjangoModelFactory):
    class Meta:
        model = Assignment

    title = Faker('name')
    description = Faker('paragraph', nb_sentences=3)
    due_date = Faker('date_object')
    subject = SubFactory(SubjectFactory)


class NoticeFactory(DjangoModelFactory):
    class Meta:
        model = Notice

    title = Faker('name')
    description = Faker('paragraph', nb_sentences=3)
    date = Faker('date_object')


class LibraryBookFactory(DjangoModelFactory):
    class Meta:
        model = LibraryBook

    title = Faker('name')
    author = Faker('first_name')
    publication_date = Faker(
        'date_object')
    availability_status = factory.fuzzy.FuzzyChoice(
        choices=[True, False])
