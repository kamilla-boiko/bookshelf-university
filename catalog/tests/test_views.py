from django.test import TestCase

from catalog.models import Author, Book, Country, LiteraryFormat

from django.urls import reverse

AUTHOR_URL = reverse("catalog:author-list")
BOOK_URL = reverse("catalog:book-list")


class AuthorListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 5 authors for pagination tests
        country = Country.objects.create(name="Ukraine")
        number_of_authors = 5
        for author_num in range(number_of_authors):
            Author.objects.create(
                first_name=f"Christian {author_num}",
                last_name=f"Surname {author_num}",
                country=country
            )

    def test_author_view_url_exists_at_desired_location(self):
        resp = self.client.get("/authors/")
        self.assertEqual(resp.status_code, 200)

    def test_author_view_url_accessible_by_name(self):
        resp = self.client.get(AUTHOR_URL)
        self.assertEqual(resp.status_code, 200)

    def test_author_view_uses_correct_template(self):
        resp = self.client.get(AUTHOR_URL)
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, "catalog/author_list.html")

    def test_author_pagination_is_three(self):
        resp = self.client.get(AUTHOR_URL)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"])
        self.assertTrue(len(resp.context["author_list"]) == 3)

    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) remaining 2 items
        resp = self.client.get(AUTHOR_URL + "?page=2")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"])
        self.assertTrue(len(resp.context["author_list"]) == 2)


class BookListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 7 books for pagination tests
        genre = LiteraryFormat.objects.create(name="poetry")
        number_of_books = 7
        for book_num in range(number_of_books):
            Book.objects.create(
                title=f"Book {book_num}",
                format=genre,
                rate=5
            )

    def test_book_view_url_exists_at_desired_location(self):
        resp = self.client.get("/books/")
        self.assertEqual(resp.status_code, 200)

    def test_book_view_url_accessible_by_name(self):
        resp = self.client.get(BOOK_URL)
        self.assertEqual(resp.status_code, 200)

    def test_book_view_uses_correct_template(self):
        resp = self.client.get(BOOK_URL)
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, "catalog/book_list.html")

    def test_book_pagination_is_five(self):
        resp = self.client.get(BOOK_URL)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"])
        self.assertTrue(len(resp.context["book_list"]) == 5)

    def test_lists_all_books(self):
        # Get second page and confirm it has (exactly) remaining 2 items
        resp = self.client.get(BOOK_URL + "?page=2")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"])
        self.assertTrue(len(resp.context["book_list"]) == 2)
