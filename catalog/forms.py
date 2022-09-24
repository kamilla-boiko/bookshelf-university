from django import forms
from catalog.models import Author, Book


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = "__all__"


class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Book
        fields = "__all__"


class BookSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title..."})
    )
    format = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by genre..."})
    )


class BookOrderForm(forms.Form):
    SORT_CHOICES = [("D", "Title"), ("ASC", "Worst"), ("DESC", "Best")]
    order = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        label="Order by:"
    )


class AuthorSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by last name..."})
    )
    country = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by country..."})
    )
