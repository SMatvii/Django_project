import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

from account.models import Profile
from products.models import Cart   

@pytest.mark.django_db
def test_profile_creation():
    user = User.objects.create_user(username='')
    profile = Profile.objects.create()
    profile = Profile.objects.get(user=user)
    cart = user.cart
    assert profile.avatar == "avatars/freak.jpg"
    assert profile.user == user
    assert profile.user == user
    assert cart.user == user