from django.db import models

# Create your models here.

class Major(models.Model):
    major_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.major_name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    belong_major = models.ForeignKey(Major, on_delete=models.CASCADE)
    prof = models.CharField(max_length=30, null=True)
    memo = models.TextField(max_length=100)

    def __str__(self):
        return self.name
