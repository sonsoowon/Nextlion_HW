from urllib import response
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.

def home(request):
    
    posts = Post.objects.all()
    return render(request, 'home.html', {"posts":posts})


def new(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            author=request.user
        )

        return redirect('detail', new_post.pk)
    
    return render(request, 'new.html')



def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    is_like = False
    if not request.user.is_anonymous:
        like = Like.objects.filter(
            post=post,
            user=request.user
        )

        if like.count() > 0:
            is_like = True

    return render(request, 'detail.html', {"post":post, "is_like": is_like})


@login_required(login_url='/registration/login')
def edit(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    if request.method == "POST":
        post.update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', post_pk)
    
    return render(request, 'edit.html', {"post": post[0]})

@login_required(login_url='/registration/login')   
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')


def login(request):
    if request.method == "POST":
        found_user, user_exists = User.objects.get_or_create(
            username=request.POST['username'],
            password='1018'
        )

        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )

        return redirect('home')
    
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required(login_url='/registration/login')
def mypage(request):
    user = User.objects.get(username=request.user)
    uploads = Post.objects.filter(author=user)


    return render(request, 'mypage.html', {"uploads": uploads})
    

@csrf_exempt
def like(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        post_pk = request_body["post_pk"]

        like, is_like = Like.objects.get_or_create(
            post=Post.objects.get(pk=post_pk),
            user=request.user
        )

        if not is_like:
            like.delete()

        post_likes = Like.objects.filter(
            post = Post.objects.get(pk=post_pk)
        )

        context = {
            'like_count' : post_likes.count(),
            'is_like' : is_like
        }

        return HttpResponse(json.dumps(context))

@csrf_exempt
def scrap(request):
    if request.method == "POST":
        request_body = json.loads(request.body)

        post_pk = request_body['post_pk']
        scrap, is_scrap = Scrap.objects.get_or_create(
            post=Post.objects.get(pk=post_pk),
            user=request.user
        )

        if not is_scrap:
            scrap.delete()

        post_scraps = Scrap.objects.filter(
            post=Post.objects.get(pk=post_pk)
        )

        context = {
            'scrap_count' : post_scraps.count(),
            'is_scrap' : is_scrap
        }

        return HttpResponse(json.dumps(context))