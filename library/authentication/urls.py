from django.urls import path
from . import views
from book.views import book_list

app_name = 'auth'
urlpatterns = [
    path('user/', views.users_info),
    path('user/<int:id>/', views.user_info),
    path('log_in/', views.log_in, name='log_in'),
    path('sign_up/', views.sign_up),
    path('book_list/', book_list, name='book'),
    path('log_out/', views.log_out, name='log_out')
]