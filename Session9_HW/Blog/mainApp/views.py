from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})



def add_post(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )

        return redirect('detail', new_post.pk)

    return render(request, 'add_post.html')

def detail_post(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    post.update(
        click_cnt = post[0].click_cnt + 1
    )

    return render(request, 'detail.html', {'post':post[0]})

def update_post(request, post_pk):
    post = Post.objects.filter(pk=post_pk)

    if request.method == 'POST':
        post.update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        
        return redirect('detail', post_pk)

    return render(request, 'update_post.html', {'post': post[0]})

def delete_post(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')