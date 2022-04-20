from django.db import models
from utils.models import Timestamps

class WaitListEnty(Timestamps,models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    notes=models.TextField()

