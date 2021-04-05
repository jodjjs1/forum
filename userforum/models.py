from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=1000)
    autor = models.CharField(max_length=50) #TODO: связь статьи и пользователя автора
    publish_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.autor}'