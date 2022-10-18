import re
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':  # create
        form = ArticleForm(request.POST)
        if form.is_valid():  # 유효성 검사
            article = form.save()      # 생성된 객체 반환
            return redirect('articles:detail', article.pk)
    else: # new
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)
   
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST': # update
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else: # edit
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)