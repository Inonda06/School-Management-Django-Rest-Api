
from django.db import models
from utils.models import Timestamps

class Lecture(Timestamps,models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    lecture_name=models.CharField(max_length=100,default='',blank=True,null=True)
    date=models.DateTimeField(auto_now=True)
    duration=models.IntegerField(help_text='Enter number of hours')
    slides_url=models.CharField(max_length=255)
    is_required=models.BooleanField(default=True)
