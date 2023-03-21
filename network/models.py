from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass

class add_post_content(models.Model):
    author=models.CharField(
        max_length=200, default=None, blank=True, null=True)
    content=models.CharField(
        max_length=200, default=None, blank=True, null=True)
    date= models.DateField()
    time=models.TimeField()

class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="user")
    post=models.ForeignKey(add_post_content,on_delete=models.CASCADE,blank=True,null=True,related_name="post")
    message=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.author} commented on {self.post}"

class Follow(models.Model):
    follower=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="follower")
    following=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="following")
    
    def __str__(self):
        return f"{self.follower} is following {self.following}"

class like(models.Model):
    liked_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="liked_user")
    liked_post=models.ForeignKey(add_post_content,on_delete=models.CASCADE,related_name="post_liked")

    def __str__(self):
        return f"{self.liked_user} liked {self.liked_post}"