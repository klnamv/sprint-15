from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from . models import Author
from book.models import Book



def authors_info(request):
    authors = list(Author.get_all())
    context = {'authors': authors}
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

    return render(request, 'remove_author.html')
