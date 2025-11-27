from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author' , 'year')
    

admin.site.register(Book, BookAdmin)
admin.site.site_header = "Books"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to the Admin Portal"