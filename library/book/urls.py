from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('book/<int:id>', views.book_info, name='book'),
    path('book/new_book', views.create_book, name='new_book'),
    path('book/remove?<int:id>', views.remove, name='remove')
]