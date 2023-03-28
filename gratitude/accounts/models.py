from django.db import models
from django.contrib.auth.models import User
from orgs.models import Org
from posts.models import Post


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    organisations = models.ManyToManyField(
        Org, related_name="organisations"
    )
    posts = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name="posts")
    

    def __str__(self):
        return self.user.username
    
    def add_post(self, post):
        self.posts.append(post)
    
    def remove_post(self, id):
        self.posts.pop(id)

    def add_organisation(self, post):
        self.organisations.append(post)
    
    def remove_organisation(self, id):
        self.organisations.pop(id)