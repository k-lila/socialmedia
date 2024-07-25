import pytest
from django.contrib.auth.models import User
from xuitter.tests.factories import UserFactory


@pytest.mark.django_db
def test_user_creation():
    user = UserFactory()
    assert User.objects.count() == 1
    assert user.username is not None
    assert user.email is not None
