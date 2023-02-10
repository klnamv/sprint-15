from django.urls import path
from . import views

app_name = 'author'
urlpatterns = [
    path('all/', views.authors_info, name='authors'),
    path('create/', views.create_author, name='add_new_author'),
    path('remove?<int:id>', views.remove_author, name='remove')
]