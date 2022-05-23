from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pubisher = models.CharField(max_length=30)
    cover = models.ImageField(blank=True, null=True)
    year_published = models.DateField()

    def __str__(self):
        return self.title


class Post(models.Model):
    POST_CATEGORY = (
        ('D', 'Debate'),
        ('Q', 'Question')
    )

    book_pk = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="posts")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    content = models.TextField()
    category = models.CharField(max_length=1, choices=POST_CATEGORY)
    page = models.DecimalField(max_digits=4, decimal_places=0, null=True)
    photo = models.ImageField(blank=True, null=True)
    
    likes = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    uploaded = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    post_pk = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")

    content = models.TextField()
    likes = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    uploaded = models.DateTimeField(auto_now_add=True)
    


