from django.test import TestCase

from catalog.models import Author, Book, Country, LiteraryFormat


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        country = Country.objects.create(name="Ukraine")
        Author.objects.create(
            first_name="Ivan",
            last_name="Franko",
            country=country
        )

    def test_author_str(self):
        author = Author.objects.get(id=1)
        self.assertEquals(str(author), f"{author.first_name} {author.last_name}")

    def test_author_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), f"/authors/{author.id}/")


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        genre = LiteraryFormat.objects.create(name="poetry")
        Book.objects.create(
            title="Kamenyary",
            format=genre,
            rate=4.9
        )

    def test_book_str(self):
        book = Book.objects.get(id=1)
        self.assertEquals(str(book), f"{book.title}")

    def test_book_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(), f"/books/{book.id}/")


class CountryModelTest(TestCase):
    def test_country_str(self):
        country = Country.objects.create(name="Ukraine")
        self.assertEquals(str(country), f"{country.name}")


class LiteraryFormatModelTest(TestCase):
    def test_country_str(self):
        genre = LiteraryFormat.objects.create(name="poetry")
        self.assertEquals(str(genre), f"{genre.name}")
