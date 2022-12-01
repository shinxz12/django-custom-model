from django.db import models
from .queryset.manager import BookListingManager, BookManagerAddFunction, BookManagerQuerysetFunc,\
    BookManagerQuerysetClass
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category, blank=True)
    objects = models.Manager()
    add_func_objects = BookManagerAddFunction()
    math_objects = BookManagerQuerysetFunc()
    queryset_custom_objects = BookManagerQuerysetClass()
    list_objects = BookListingManager()

    def __str__(self) -> str:
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=255)
    discount_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percentage = models.DecimalField(
        max_digits=5, decimal_places=3, null=True, blank=True)
    book = models.ManyToManyField(Book, blank=True)

    def __str__(self) -> str:
        return self.name
