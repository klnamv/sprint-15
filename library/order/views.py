from datetime import datetime, timedelta

from django.shortcuts import render
from order.models import Order
from authentication.models import CustomUser
from book.models import Book
from django.views.decorators.csrf import csrf_exempt


def orders_by_librarian(request):
    orders = Order.get_all()
    context = {'orders': orders}
    return render(request, 'librarian_orders.html', context)


def orders_by_user(request, id):
    orders = list(Order.objects.filter(user_id=id).values())
    context = {'orders': orders}
    return render(request, 'user_orders.html', context)


@csrf_exempt
def create_order(request, id):
    book_id = request.POST.get('book_id')
    print(f'response: {book_id}')
    Order.create(CustomUser.objects.get(id=id), Book.objects.get(id=book_id),
                 plated_end_at=datetime.today() + timedelta(days=20))
    return render(request, 'create_order.html')


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
