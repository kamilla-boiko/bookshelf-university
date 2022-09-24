from django.contrib import admin

from catalog.models import LiteraryFormat, Country, Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "format", "rate"]
    list_filter = ["format"]
    search_fields = ["title"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "country",
                    "birth_date", "death_date", "sex"]
    list_filter = ["country"]
    search_fields = ["last_name"]


admin.site.register(LiteraryFormat)
admin.site.register(Country)
