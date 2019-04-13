from django.db import models
from django.urls import reverse
from uuid import uuid4

# Create your models here.

class Genre(models.Model):
    """Model representing a genre book"""

    name = models.CharField(max_length=200, help_text="Enter a book genre (eg. Science, Fiction)")

    def __str__(self):
        """String representation Model object"""
        return self.name


class Book(models.Model):
    """Model representing a logical book"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description about the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='Enter 13 character ISBN')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String representing Model object"""
        return self.title

    def get_absolute_url(self):
        """Returns the detail of specified book"""
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """For admin site to display genre of book"""
        return  ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    """Model representing an actual book instance"""

    id = models.UUIDField(primary_key=True, default=uuid4, help_text='Unique ID for a book instance accross library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, help_text='Book availability', blank=True, default='m')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String representing Model object"""
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """Moel representing an author"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField('Died', blank=True, null=True)

    def __str__(self):
        """String representing an author"""
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        """Returns the detail of specified author"""
        return reverse('author-detail', args=[str(self.id)])

    class Meta:
        ordering = ['last_name', 'first_name']


class Language(models.Model):
    """Model representing a language of a book"""

    name = models.CharField(max_length=200, help_text='Enter the natural language of the book (e.g. English, French...)')

    def __str__(self):
        """String representation of a language"""
        return self.name
