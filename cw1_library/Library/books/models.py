from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author)
    description = models.TextField()
    isbn = models.CharField(max_length=13)
    


    def __str__(self):
        return self.title

class Memeber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()
    contact_number = models.IntegerField()
    address = models.CharField(max_length=200)
    book_borrowed = models.ManyToManyField(Book, through='BorrowedBook')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class BorrowedBook (models.Model):
    member = models.ForeignKey(Memeber,on_delete=models.RESTRICT)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    borrowed_date = models.DateField()
    return_date = models.DateField(null=True,blank=True)
    deadline_date = models.DateField()
    def __str__(self):
        return f'{self.member} - {self.book}'