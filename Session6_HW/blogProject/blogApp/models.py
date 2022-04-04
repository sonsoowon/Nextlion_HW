from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.title
