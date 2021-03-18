from django.shortcuts import render, get_object_or_404
from .models import Post


def all_blogs(request):
    posts = Post.objects.all()
    # posts = Post.objects.order_by('-date')[:5]

    return render(request, "blog/all_blogs.html", {"title": "Blog", "posts": posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    title = post.title
    return render(request, "blog/detail.html", {"title": title, "post": post})
