from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author':'ray',
        'title':'blog post 1',
        'content':'first post content',
        'date_posted':'December 9, 1999'
    },
    {
        'author':'ray',
        'title':'blog post 2',
        'content':'second post content',
        'date_posted':'December 25, 1999'
    }]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def privacyPolicy(request):
    return render(request, 'blog/privacypolicy.html')
