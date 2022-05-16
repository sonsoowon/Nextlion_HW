from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    upload_time = models.DateTimeField(auto_now_add=True)
    click_cnt = models.DecimalField(max_digits=3, decimal_places=0, default=0)

    class Meta:
        ordering = ['-upload_time']
