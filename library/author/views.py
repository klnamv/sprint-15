from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from . models import Author
from book.models import Book



def authors_info(request):
    # authors = [author for author in  if str(author.books) != "book.Book.None"]
    authors = Author.get_all()
    new_authors = []

    for author in authors:
        new_author_books = list(Book.objects.filter(authors=author))
        book_names = ', '.join(book.name for book in new_author_books)
        new_author = {
            'name': author.name,
            'surname': author.surname,
            'patronymic': author.patronymic,

        }
        if not new_author_books:
            new_author['books'] = "No books"
        else:
            new_author['books'] = book_names
        new_authors.append(new_author)

    context = {'authors': new_authors}

    return render(request, 'authors_info.html', context)


@csrf_exempt
def create_author(request):
    name = request.POST.get('author_name')
    surname = request.POST.get('surname')
    patronymic = request.POST.get('patronymic')
    Author.create(name, surname, patronymic)

    return render(request, 'create_author.html')


@csrf_exempt
def remove_author(request):
    author_id = request.POST.get('author_id')
    author = Author.get_by_id(author_id)

    if len(Book.objects.filter(authors=author)) <= 0:
        Author.delete_by_id(author_id)

    return render(request, 'remove_author.html', status=400)
