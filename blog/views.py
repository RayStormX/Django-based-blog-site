from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return HttpResponse('<h1>blog about page</h1>')

def privacyPolicy(request):
    return HttpResponse("you're not really going to read this")