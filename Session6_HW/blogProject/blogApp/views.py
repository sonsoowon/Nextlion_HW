from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    if request.method == 'POST':
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            tag = request.POST['tag']
        )
        
        return redirect('list')
    return render(request, 'new.html')

def list_all(request):
    all_articles = Article.objects.all()

    all_cnt = all_articles.count()
    hobby_cnt = all_articles.filter(tag='hobby').count()
    food_cnt = all_articles.filter(tag='food').count()
    program_cnt = all_articles.filter(tag='programming').count()

    return render(request, 'list.html', {
        'articles': all_articles,
        'all_cnt' : all_cnt,
        'hobby_cnt' : hobby_cnt,
        'food_cnt' : food_cnt,
        'program_cnt' : program_cnt
    })



def list_filtered(request, tag):

    all_articles = Article.objects.all()
    articles = all_articles.filter(tag=tag)

    all_cnt = all_articles.count()
    hobby_cnt = all_articles.filter(tag='hobby').count()
    food_cnt = all_articles.filter(tag='food').count()
    program_cnt = all_articles.filter(tag='programming').count()

    return render(request, 'list.html', {
        'articles': articles,
        'all_cnt' : all_cnt,
        'hobby_cnt' : hobby_cnt,
        'food_cnt' : food_cnt,
        'program_cnt' : program_cnt
    })



def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article': article})