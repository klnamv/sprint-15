from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from order.models import Order
from authentication.models import CustomUser
from book.models import Book
from django.views.decorators.csrf import csrf_exempt


def orders_by_librarian(request):
    if request.user.role != 1:
        return redirect('order:order', id=request.user.id)
    orders = Order.get_all()
    # orders = list(Order.objects.all().distinct().values())
    new_orders = []
    for order in orders:
        try:
            print(order.user_id)
            client = CustomUser.get_by_id(order.user_id)
            #client = CustomUser.objects.get(id=order.user_id)
            books = Book.objects.get(id=order.book_id).name
            new_order = {
                'id': order.id,
                'created_at': order.created_at,
                'end_at': order.end_at,
                'plated_end_at': order.plated_end_at.date(),
                'client_info': f"{client.first_name} {client.last_name}",
                'books': books,
            }
            print(new_order)
            new_orders.append(new_order)
        except Exception as e:
            print(e)
    context = {'orders': new_orders}
    return render(request, 'librarian_orders.html', context)


def orders_by_user(request, id):
    user = CustomUser.get_by_id(id)
    # orders = list(Order.objects.filter(user_id=id).values())
    orders = Order.objects.filter(user=user.id)
    new_orders = []
    reader = ''
    try:

        for order in orders:
            client = CustomUser.get_by_id(order.user_id)
            books = Book.objects.get(id=order.book_id).name
            new_order = {
                'id': order.id,
                'created_at': order.created_at,
                'end_at': order.end_at,
                'plated_end_at': order.plated_end_at.date(),
                'client_info': f"{client.first_name} {client.last_name}",
                'books': books,
            }
            new_orders.append(new_order)
            reader = new_order['client_info']
    except Exception as e:
        print(e)
    context = {
        'reader': reader,
        'orders': new_orders
    }
    return render(request, 'user_orders.html', context)


@csrf_exempt
def create_order(request, id):
    try:
        book_id = id
        book = Book.get_by_id(book_id)
        if book.count <= 0:
            return redirect('book:book_list')
        user_id = request.user.id
        print(f'response: {book_id}')
        print(CustomUser.get_by_id(user_id))
        order = Order.create(CustomUser.get_by_id(user_id), Book.objects.get(id=book_id),
                 plated_end_at=datetime.today() + timedelta(days=20))
        book.update(count = book.count - 1)
    except Exception as e:
        print(e)
    return redirect('book:book_list')


@csrf_exempt
def close_order(request):
    order_id = request.POST.get('order_id')
    try:
        order = Order.get_by_id(order_id)
        order.update(end_at=datetime.today())
        Order.delete_by_id(order_id)
    except Exception:
        pass
    return render(request, 'close_order.html')
