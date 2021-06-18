from django.db import models
from login_app.models import *
# Create your models here.

class Message(models.Model):
    message = models.TextField()
    poster = models.ForeignKey(User, related_name="user_message", on_delete = models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    commentor = models.ForeignKey(User, related_name="user_comment", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
