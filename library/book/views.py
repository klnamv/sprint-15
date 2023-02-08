from django.shortcuts import render, redirect
from . models import Book

def book_list(request):
    # Book.create('Гаррі Поттер і філософський камінь', 'Перша частина пригод Гаррі Поттера'
    #                                                   '— книга №1 для маленьких читачів.'
    #                                                   'Саме вона сколихнула хвилю любові',
    #             authors=[])
    books = Book.get_all()
    context = {'books': books}
    print(books[0])
    if request.user.is_authenticated:
        if request.method == 'POST':
            filtered_books = []
            text = request.POST['search']
            print(text)
            for book in books:
                if text in book.name or text in book.description:
                    filtered_books.append(book)
            context['books']=filtered_books
        print(request.user)
        return render(request, "book_list.html", context)
    else:
        return redirect('auth:log_in')


def book_info(request, id):
    book = Book.get_by_id(id)
    context = {'book': book}
    return render(request,'book.html', context)

def create(request):
    if request.user.role != 1:
        return redirect('book:book_list')