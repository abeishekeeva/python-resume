from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('general', views.post_list_other, name='post_list_general'),
    path('books', views.post_list_books, name='post_list_books'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]