from django.db import models
from django.contrib.auth.models import User  # the "User" from the admin panel

# Create your models here.

class Twitter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #learn what is cascade
    text=models.TextField(max_length=500)
    photo=models.ImageField(upload_to='twitters',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}-{self.text[:20]}'

