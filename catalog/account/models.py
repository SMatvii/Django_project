from django.db import models
from django.contrib.auth.models import User
from products.models import Category


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/freak.jpg", blank=True)
