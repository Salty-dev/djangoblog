from django.contrib import admin
from blog.models import Category, Author, Post

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
