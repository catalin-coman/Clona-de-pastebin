from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def get_absolute_url(self):
        return reverse('textbin:userlist', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Text(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)

    def get_absolute_url(self):
        return reverse('textbin:home')

    def __str__(self):
        return self.title + self.content
