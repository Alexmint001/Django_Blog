from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(default = user, max_length=64)
    profile_image = models.ImageField(default='#', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
# Create your models here.

