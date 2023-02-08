from django.urls import path
from . import views

app_name = 'author'
urlpatterns = [
    path('all/', views.authors_info, name='authors'),
    path('create/', views.create_author),
    path('remove/', views.remove_author)
]