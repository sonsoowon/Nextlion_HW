from wsgiref.util import setup_testing_defaults
from django.utils import timezone
from email.policy import default
from xml.etree.ElementInclude import default_loader
from datetime import date
from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    deadline = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    def dday(self):
        remains = (self.deadline - timezone.now().date()).days
        if remains > 0:
            return "D-" + str(remains)
        elif remains == 0:
            return "D-day"
        else:
            return "D+" + str(abs(remains))
    
    class Meta:
        ordering = ['deadline']





