from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.
"""
dummy data

posts=[
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

"""

"""
class-based views
"""
class PostListView(ListView):
    """
    tells our ListView what model to query in order to create the list
    """
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

def privacyPolicy(request):
    return render(request, 'blog/privacypolicy.html')
