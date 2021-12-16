from django.contrib import admin
from .models import Author, Genre, Book, Publisher, Discount

# Register your models here.
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Discount)


class BookInline(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'date_of_birth', 'date_of_death')
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death'), 'bio']
    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'released_date', 'publisher')
    list_filter = ('publisher', 'genre')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_bio')