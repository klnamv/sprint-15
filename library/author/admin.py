from django.contrib import admin
from book.admin import AuthorsInline
from .models import Author

@admin.display(description='BOOK NAME')
def book_names(obj):
    book_n = []
    for book in list(obj.books.all()):
        book_n.append(book.name)
    new_line = "  |  "
    return f'{new_line.join(book_n)}'

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        AuthorsInline,
    ]

    # readonly_fields = ['name', 'surname', 'patronymic']

    list_display = ('id', 'name', 'surname', 'patronymic', book_names)

    list_display_links = ('name', 'surname')

    fields = ['name', 'surname', 'patronymic']

    search_fields = ['books__name', 'name', 'surname']

    list_filter = ['name', 'surname', ('books__name', custom_titled_filter('book'))]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'surname', 'patronymic']
        else:
            return []

admin.site.register(Author, AuthorAdmin)
