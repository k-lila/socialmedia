import pytest
from xuitter.tests.factories import UserFactory, ProfileFactory
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from xuitter.models import Profile, create_profile


@pytest.fixture(autouse=True)
def disconnect_signals():
    post_save.disconnect(create_profile, sender=User)
    yield
    post_save.connect(create_profile, sender=User)


@pytest.mark.django_db
def test_profile_creation():
    user = UserFactory()
    profile = ProfileFactory(user=user)
    assert Profile.objects.count() == 1
    assert profile.user == user
    assert profile.profile_image is not None
    assert profile.profile_bio is not None
    assert profile.profile_website is not None
