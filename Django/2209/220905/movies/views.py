from django.shortcuts import render, redirect
from .forms import MovieForm

# Create your views here.
def index(request):
    
    return render(request, 'movies/index.html')

def new(request):
    form = MovieForm()
    context = {
        'form': form,

    }
    return render(request, 'movies/new.html', context)

def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    genre = request.POST.get('genre')
    decription = request.POST.get('decription')

    movie = MovieForm(
        title = title,
        audience =  audience,
        genre = genre,
        decription = decription,

    )
    movie.save()
    return redirect('movies:index')