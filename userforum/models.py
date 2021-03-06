from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=1000)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    publish_time = models.DateTimeField(auto_now_add=True, null=True)
    views_count = models.PositiveIntegerField(null=True, blank=False)
    genre = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.title} by {self.autor}'
