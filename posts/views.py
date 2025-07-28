from django.shortcuts import render
from datetime import datetime
from .models import Post

def posts(request):
    posts = Post.objects.filter(is_published=False).order_by('-created_at')
    context = {
        'posts': posts,
        'year': datetime.now().year
    }
    return render(request, "posts.html", context)

def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
        'year': datetime.now().year
    }
    return render(request, "post_detail.html", context)