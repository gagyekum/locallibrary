from django.contrib import admin
from .models import Book, BookInstance, Language, Genre, Author

# Register your models here.

# Catalog model registrations
#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)
#admin.site.register(Author)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {'fields': ('id', 'book', 'imprint')}),
        ('Availability', {'fields': ('status', 'due_back')})
    )

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

class BookInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))
    inlines = [BookInline]
