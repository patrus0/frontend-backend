from django.contrib import admin

from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_display_links = ('title', )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Books, BookAdmin)
admin.site.register(Author, AuthorAdmin)
