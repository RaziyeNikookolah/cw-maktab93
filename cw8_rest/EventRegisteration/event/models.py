from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=400)
    phone_number = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title


class ParticipantShip(models.Model):
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="participantShips")
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="participantShips")
    

    def __str__(self) -> str:
        return super().__str__()