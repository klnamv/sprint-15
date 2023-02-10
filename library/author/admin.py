from django.contrib import admin
from book.admin import AuthorsInline
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        AuthorsInline,
    ]
    list_display = ('id', 'name', 'surname', 'patronymic')


admin.site.register(Author, AuthorAdmin)
