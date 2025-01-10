from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(is_published=True)
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})

def tag_posts(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag, is_published=True)
    return render(request, 'blog/tag_posts.html', {'tag': tag, 'posts': posts})
