from django.core import paginator
from django.shortcuts import render
from .models import Genre, Book
from django.views import generic
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    science_books = Book.objects.filter(genre__name__icontains='Ảo')
    vn_books = Book.objects.filter(genre__name__icontains='Việt Nam')
    life_books = Book.objects.filter(genre__name__contains='Sống')

    context = {
        'science_books': science_books,
        'vn_books': vn_books,
        'life_books': life_books

    }
    return render(request, 'index.html', context)


def about_us(request):
    return render(request, 'about.html')


class BookListView(generic.ListView):
    # return render(request, 'products.html')   
    model = Book
    paginate_by = 9

class BookDetailView(generic.DetailView):
    model = Book

def science_books(request, gen):
    if gen == 'science':
        keyword = 'Ảo'
    elif gen == 'vietnam':
        keyword = 'Việt'
    elif gen == 'life':
        keyword = 'Đời'
    
    book_list = Book.objects.filter(genre__name__contains=keyword)
    genre = Genre.objects.get(name__contains=keyword)

    paginator = Paginator(book_list, 9) # Show 9 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'book_list': book_list,
        'genre': genre,
        'page_obj': page_obj,
        'is_paginated': True if paginator.num_pages > 1 else False,
    }
    return render(request, 'hexashop/book_list.html', context)


def single_product(request):
    return render(request, 'single_product.html')


def contact(request):
    return render(request, 'contact.html')