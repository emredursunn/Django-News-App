from django.shortcuts import render, redirect, get_object_or_404
from .models import News, Category
# Create your views here.

def index(request):
    context = {
        "data": News.objects.all(),
        "categories":Category.objects.all(),
    }
    return render(request, 'news/index.html', context)

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    context = {
        "news": news
    }
    return render(request, 'news/newsDetail.html', context)

def get_news_by_category(request, slug):
    context = {
        "data": News.objects.filter(category__slug=slug),
        "categories":Category.objects.all(),
    }
    return render(request, 'news/index.html', context)


