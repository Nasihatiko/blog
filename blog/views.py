from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def posts_lists(request):
    n = ['Suh', 'Nas', 'Mariam', 'Nozmina']
    return render(request, 'blog/index.html', context={'names': n})