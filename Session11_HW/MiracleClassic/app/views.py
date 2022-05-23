
from django.shortcuts import render, redirect
from .models import *

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    debates = Post.objects.filter(category="D")[:3]
    questions = Post.objects.filter(category="Q")[:3]

    return render(request, 'home.html', {
        "debates":debates,
        "questions":questions
    })

def post_list(request, category):
    posts = Post.objects.all()
    if category == "debates":
        posts = posts.filter(category="D")
    elif category == "questions":
        posts = posts.filter(category="Q")
    
    return render(request, 'post_list.html', {"posts":posts})

def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        new_comment = Comment.objects.create(
            post_pk = post,
            writer = user,
            content = request.POST['content']
        )
        return redirect('post_detail', post_pk)
    

    return render(request, 'post_detail.html', {"post":post})


def edit_post(request, post_pk):
    post = Post.objects.filter(pk=post_pk)

    if request.method == 'POST':
        post.update(
            content = request.POST['content'],
            category = request.POST['category'],
            page = request.POST['page']
        )
        return redirect('post_detail', post_pk)

    return render(request, 'edit_post.html', {"post":post[0]})


def delete_post(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()

    return redirect('post_detail', post_pk)

@login_required(login_url='accounts/kakao/login')
def new_post(request):
    books = Book.objects.all()
    if request.method == 'POST':
        book_pk = Book.objects.get(pk=request.POST['book'])
        user = User.objects.get(username=request.user)
        new_post = Post.objects.create(
            book_pk = book_pk,
            writer = user,
            category = request.POST['category'],
            photo = request.FILES['photo'],
            page = request.POST['page'],
            content = request.POST['content']
        )

        return redirect('post_detail', new_post.pk)
    
    return render(request, 'new_post.html', {"books":books})

def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    
    return render(request, 'book_detail.html', {"book":book})

    

def logout(request):
    auth.logout(request)
    return redirect('home')