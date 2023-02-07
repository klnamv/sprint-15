from django.urls import path
from . import views
urlpatterns = [
    path('all/', views.authors_info),
    path('create/', views.create_author),
    path('remove/', views.remove_author)
]