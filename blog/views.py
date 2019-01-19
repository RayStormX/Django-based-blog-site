from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import(
    ListView,
    DetailView,
    CreateView
)
# Create your views here.


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

class PostCreateView(CreateView):
    model = Post
    fields =['title','content']


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

def privacyPolicy(request):
    return render(request, 'blog/privacypolicy.html')
