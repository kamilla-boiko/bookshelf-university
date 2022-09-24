from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class LiteraryFormat(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name


class Author(models.Model):
    GENDER_CHOICES = [("M", "man"), ("W", "woman")]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="authors"
    )
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to="photos/", null=True, blank=True)
    bio = models.TextField()

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse("catalog:author-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    format = models.ForeignKey(
        LiteraryFormat,
        on_delete=models.CASCADE,
        related_name="books"
    )
    authors = models.ManyToManyField(Author, related_name="books")
    book_hyperlink = models.URLField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        ordering = ["title"]

    def get_absolute_url(self):
        return reverse("catalog:book-detail", args=[str(self.id)])

    def __str__(self):
        return self.title
