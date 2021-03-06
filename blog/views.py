from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), tag="programming").order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_list_other(request):
    posts_other = Post.objects.filter(published_date__lte=timezone.now(), tag="general").order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts_other': posts_other})

def post_list_books(request):
    posts_books = Post.objects.filter(published_date__lte=timezone.now(), tag="books").order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts_other': posts_books})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})