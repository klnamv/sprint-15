from django.contrib import admin
from .models import Book


class AuthorsInline(admin.TabularInline):
    model = Book.authors.through

@admin.display(description='AUTHOR')
def author_names(obj):
    author_n = []
    for author in list(obj.authors.all()):
        author_n.append(f'{author.name} {author.surname}')
    new_line = "  |  "
    return f'{new_line.join(author_n)}'

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper

class BookAdmin(admin.ModelAdmin):

    inlines = [
        AuthorsInline,
    ]

    exclude = ['authors']

    list_display = ('name', 'description', 'count', author_names, 'id')

    # readonly_fields = ('name', 'description', )

    list_filter = ('id', 'name', ('authors__surname', custom_titled_filter('author')))

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'description', 'publication_date']
        else:
            return []

    fieldsets = (
        ('Non changeable', {
            'fields': ('name', 'description', 'publication_date')
        }),
        ('Changeable', {
            'fields': ('count', 'issue_date')
        })
    )


admin.site.register(Book, BookAdmin)

