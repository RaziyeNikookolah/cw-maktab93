from factory import Faker, SubFactory, LazyAttribute
from factory.django import DjangoModelFactory
from faker.providers import person, misc
from .models import Student, Address


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
    name = Faker('first_name')
    # subject = models.CharField("the subject taught by the teacher", required=True, max_length=100)
    subject = SubFactory(lambda: SubjectFactory())
    date_of_birth = Faker('date_of_birth', minimum_age=18, maximum_age=65, provider=person)
    gender = Faker('random_element', elements=["F", "M"], provider=misc)
    address = SubFactory(lambda: AddressFactory())
    email = LazyAttribute(lambda o: '%s@example.com' % o.name)
