from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import AuthorForm, BookForm, BookSearchForm, AuthorSearchForm, BookOrderForm
from catalog.models import Book, Author


def index(request):
    num_books = Book.objects.count()
    num_authors = Author.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_visits": num_visits + 1
    }

    return render(request, "catalog/index.html", context=context)


def genre_list(request):
    books = Book.objects.all().values("format__name")
    genres = []
    for item in books:
        if item["format__name"] not in genres:
            genres.append(item["format__name"])

    context = {
        "genres": genres
    }

    return render(request, "catalog/literary_format_list.html", context=context)


def country_list(request):
    authors = Author.objects.all().values("country__name")
    countries = []
    for item in authors:
        if item["country__name"] not in countries:
            countries.append(item["country__name"])

    context = {
        "countries": countries
    }

    return render(request, "catalog/country_list.html", context=context)


class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.all().select_related("format")
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")
        format_ = self.request.GET.get("format", "")
        order = self.request.GET.get("order", "")

        context["search_form"] = BookSearchForm(
            initial={"title": title, "format": format_}
        )
        context["order_form"] = BookOrderForm(
            initial={"order": order}
        )

        return context

    def get_queryset(self):
        form = BookSearchForm(self.request.GET)
        order = BookOrderForm(self.request.GET)

        if form.is_valid():
            self.queryset = self.queryset.filter(
                title__icontains=form.cleaned_data["title"]
            ).filter(
                format__name__icontains=form.cleaned_data["format"]
            )
        if order.is_valid():
            if order.cleaned_data["order"] == "DESC":
                self.queryset = self.queryset.order_by("-rate")
            elif order.cleaned_data["order"] == "ASC":
                self.queryset = self.queryset.order_by("rate")
            else:
                self.queryset = self.queryset
        return self.queryset


class BookDetailView(generic.DetailView):
    model = Book


class BookCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("catalog:book-list")


class BookUpdateView(generic.UpdateView):
    model = Book
    form_class = BookForm


class AuthorListView(generic.ListView):
    model = Author
    queryset = Author.objects.all()
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)

        last_name = self.request.GET.get("last_name", "")
        country = self.request.GET.get("country", "")

        context["search_form"] = AuthorSearchForm(
            initial={"last_name": last_name, "country": country}
        )

        return context

    def get_queryset(self):
        form = AuthorSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                last_name__icontains=form.cleaned_data["last_name"]
            ).filter(
                country__name__icontains=form.cleaned_data["country"]
            )
        return self.queryset


class AuthorDetailView(generic.DetailView):
    model = Author
    queryset = Author.objects.all().prefetch_related("books__format")


class AuthorCreateView(generic.CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("catalog:author-list")


class AuthorUpdateView(generic.UpdateView):
    model = Author
    form_class = AuthorForm


def test_session_view(request):
    return HttpResponse(
        "<h1>Test Session</h1>"
        f"<h4>Session data: {request.session['book']}</h4>"
    )
