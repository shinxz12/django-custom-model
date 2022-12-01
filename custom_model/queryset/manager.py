from django.db.models.functions import Coalesce
from django.db import models
from django.db.models import QuerySet
from django.db.models.manager import BaseManager

from custom_model.queryset.raw_queryset import BookRawQueryset


class BookManagerAddFunction(models.Manager):
    def with_counts(self):
        return self.annotate(
            num_responses=Coalesce(models.Count("category"), 0)
        )

    @property
    def math(self):
        return self.filter(category__name__icontains="Math")


class BookManagerQuerysetFunc(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category__name__icontains="Math")


class BookQuerySet(models.QuerySet):
    def math(self):
        return self.filter(category__name__icontains="Math")

    def other(self):
        return self.filter(category__name__icontains="Other")


class BookManagerQuerysetClass(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, using=self._db)

    @property
    def math(self):
        return self.get_queryset().math()

    @property
    def other(self):
        return self.get_queryset().other()


class BookListingManager(BaseManager.from_queryset(QuerySet)):
    def custom_filter(self):
        from custom_model.models import Book
        queryset = BookRawQueryset()
        queryset.model = Book
        return queryset
