from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    is_draft = models.BooleanField(default=True)
    author = models.ForeignKey('users.User',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title:.30}"

    def save(self, *args, **kwargs):
        if not self.is_draft and not self.published_at:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)
