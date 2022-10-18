from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'articles/index.html')

def new(request):

    return render(request, 'articles/new.html')

def create(request):

    return render(request, 'articles/create.html')