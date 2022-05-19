from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    clicks = models.DecimalField(max_digits=3, decimal_places=0, default=0)

    uploaded = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    uploaded = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content