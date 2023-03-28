from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from accounts.models import UserProfile

# Create your models here.

class Post(models.Model):
    # author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=255)
    message = models.TextField()
    recipients = models.ManyToManyField(User, related_name="recipients")
    visit_date = models.DateTimeField()
    post_date = models.DateTimeField(default=timezone.now)
    stars = models.IntegerField()
    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/', default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLrWVtomuKNMXY38fiZ6HM7PJSiE7ubfdfvQbdAXC9&s")

    def __str__(self):
        return self.title