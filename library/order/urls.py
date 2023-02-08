from django.urls import path, include
from . import views

app_name = 'order'
urlpatterns = [
    path('all/', views.orders_by_librarian, name='orders'),
    path('user?<int:id>/', views.orders_by_user, name='order'),
    path('create?<int:id>/', views.create_order, name='create_order'),
    path('close/', views.close_order)
]