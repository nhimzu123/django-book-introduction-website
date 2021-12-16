from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_us, name='about'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('books/<str:gen>', views.science_books, name='books-gen'),
    path('single-product', views.single_product, name='single-product'),
    path('contact', views.contact, name='contact'),
]