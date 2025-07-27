from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import Post

def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'year': datetime.now().year
    }
    return render(request, "posts.html", {'posts': posts})

def post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "post_detail.html", {'post': post})