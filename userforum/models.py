from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=1000)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(auto_now=False)
    views_count = models.PositiveIntegerField(null=True, blank=False)

    def __str__(self):
        return f'{self.title} by {self.autor}'
