from django.urls import path

from catalog.views import (
    index,
    genre_list,
    country_list,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    test_session_view,
    AuthorListView,
    AuthorDetailView,
    AuthorCreateView,
    AuthorUpdateView
)

urlpatterns = [
    path("", index, name="index"),
    path("test-session/", test_session_view, name="test-session"),
    path(
        "literary-formats/",
        genre_list,
        name="literary-format-list"
    ),
    path(
        "countries/",
        country_list,
        name="country-list"
    ),
    path(
        "books/",
        BookListView.as_view(),
        name="book-list"
    ),
    path(
        "books/<int:pk>/",
        BookDetailView.as_view(),
        name="book-detail"
    ),
    path(
        "books/create/",
        BookCreateView.as_view(),
        name="book-create"
    ),
    path(
        "books/<int:pk>/update/",
        BookUpdateView.as_view(),
        name="book-update"
    ),
    path(
        "authors/",
        AuthorListView.as_view(),
        name="author-list"
    ),
    path(
        "authors/<int:pk>/",
        AuthorDetailView.as_view(),
        name="author-detail"
    ),
    path(
        "authors/create/",
        AuthorCreateView.as_view(),
        name="author-create"
    ),
    path(
        "authors/<int:pk>/update/",
        AuthorUpdateView.as_view(),
        name="author-update"
    ),
]

app_name = "catalog"
