from django.urls import path

from book import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
]