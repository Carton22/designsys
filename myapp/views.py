from django.shortcuts import render,redirect
from .models import Post

def create_post(request):
    if request.method == 'POST':
        text = request.POST['text']
        Post.objects.create(text=text)
        return redirect('create_post')

    posts = Post.objects.all()
    return render(request, 'create_post.html', {'posts': posts})

def display_post(request):
    posts = Post.objects.all()
    return render(request, 'display_post.html', {'posts': posts})

def clear_post(request):
    if request.method == 'POST':
        Post.objects.all().delete()
    return redirect('create_post')