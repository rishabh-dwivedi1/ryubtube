from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    thumbnail = models.ImageField(
        upload_to='thumbnails/'
    )

    video = models.FileField(
        upload_to='videos/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    views = models.IntegerField(default=0)

    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):

    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.username