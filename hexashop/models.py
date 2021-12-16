from functools import update_wrapper
from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import FloatField
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    """Representing the book's genre"""
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    bio = models.TextField(help_text='Something about this author')

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def display_name(self):
        return f'{self.first_name} {self.last_name}'
    
    display_name.short_description = 'Name'


class Genre(models.Model):
    name = models.CharField(max_length=40, help_text='The name of genre xD')
    short_bio = models.CharField(max_length=50, help_text='A brief description of this genre.')

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=30, help_text='Name of the publisher.')
    est_date = models.DateField('Established date', null=True, blank=True)

    def __str__(self):
        return self.name


class Discount(models.Model):
    code = models.CharField('Coupon code', max_length=10)
    percent = models.IntegerField(help_text='Enter how much the store wants to sale off.')

    class Meta:
        ordering = ['code']

    def __str__(self):
        return f'This book is off {str(self.percent)}%'


class Book(models.Model):
    title = models.CharField(max_length=40, help_text='Title of the book')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, help_text='Select genre for this book (e.g. Science Fiction).')
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=SET_NULL, null=True, blank=True)

    released_date = models.DateField(help_text='The day that book was released.')
    description = models.TextField(max_length=1000, help_text='Something about this book.')
    image = models.ImageField(upload_to='uploads/', help_text='Upload the facebook.', null=True, blank=True)
    price = models.IntegerField()

    class Meta:
        ordering = ['-released_date', 'title', 'publisher']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join([gen.name for gen in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def get_discount_price(self):
        if self.discount:
            return int(self.price*(100-self.discount.percent)/100)
        return self.price
