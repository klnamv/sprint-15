from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users_info),
    path('user/<int:id>/', views.user_info)
]