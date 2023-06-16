from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author)
    description = models.TextField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title