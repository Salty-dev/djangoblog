from django.shortcuts import render
from django.views.generic.detail import DetailView
from blog.models import Post

def blog(request):
    context = {}
    return render(request, 'blog/blog.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_field = 'slug'
