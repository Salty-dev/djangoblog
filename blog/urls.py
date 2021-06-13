from django.urls import path
from blog.views import blog, post

urlpatterns = [
    path('', blog, name='blog'),
    path('post', post, name='post'),
]
