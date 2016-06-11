from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html', {})

def blog(request):
    return render(request, 'home/blog.html', {})

def about(request):
    return render(request, 'home/about.html', {})

def contact(request):
    return render(request, 'home/contact.html', {})