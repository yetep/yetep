from django.shortcuts import render
from django.utils import timezone
from .models import Post

def home(request):
    return render(request, 'home/home.html', {})

#def blog(request):
#    return render(request, 'home/blog.html', {})

def about(request):
    return render(request, 'home/about.html', {})

def contact(request):
    return render(request, 'home/contact.html', {})

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home/blog.html', {'posts': posts})