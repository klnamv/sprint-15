from django.contrib import admin
from .models import Book


class AuthorsInline(admin.TabularInline):
    model = Book.authors.through


class BookAdmin(admin.ModelAdmin):

    inlines = [
        AuthorsInline,
    ]

    exclude = ['authors']
    list_display = ('id', 'name', 'description', 'count', 'get_authors')
    list_filter = ('id', 'name', 'authors')


admin.site.register(Book, BookAdmin)

