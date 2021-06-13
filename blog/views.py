from django.shortcuts import render

def blog(request):
    context = {}
    return render(request, 'blog/blog.html', context)

def post(request):
    context = {}
    return render(request, 'blog/post.html', context)