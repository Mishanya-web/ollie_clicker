from django.db import models
from django.contrib.auth.models import User

class Gamer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.user.username}'