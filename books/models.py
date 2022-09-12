from django.db import models
from django.shortcuts import reverse


class Book(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    BOOK_LANGUAGE = (
        ('lge', 'persian'),
        ('lge', 'english'),
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    translator = models.CharField(max_length=100, null=True, blank=True)
    publisher = models.CharField(max_length=100)
    year_of_publication = models.IntegerField()
    number_of_pages = models.IntegerField()
    language = models.CharField(max_length=50, choices=BOOK_LANGUAGE, default='persian')

    def __str__(self):
        return self.title

