from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('book/<int:id>', views.book_info, name='book')
]