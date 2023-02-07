from django.urls import path, include
from . import views
urlpatterns = [
    path('all/', views.orders_by_librarian),
    path('user/<int:id>/', views.orders_by_user),
    path('create/<int:id>/', views.create_order),
    path('close/', views.close_order),
]