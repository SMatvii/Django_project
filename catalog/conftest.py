import django
import os
import pytest

from django.contrib.auth.models import User


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catalog.settings")
django.setup()


@pytest.fixture
def user():
    return User.objects.create_user(
        username="user",
        password="1234"
    )