from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Amanda',
        'title': 'Blog Post 1',
        'content': 'Fist Post Content',
        'date_posted': 'December, 27th, 2022'
    },
    {
        'author': 'Josh Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'December, 27th, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
