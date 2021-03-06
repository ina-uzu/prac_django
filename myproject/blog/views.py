from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request,'blog/post_list.html',context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)