from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    intro_text = models.TextField( blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    tag = models.CharField(max_length=200, default="general")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title