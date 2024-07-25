import pytest
from xuitter.models import Post
from xuitter.tests.factories import UserFactory, PostFactory


@pytest.mark.django_db
def test_post_creation():
    user = UserFactory()
    post = PostFactory(user=user)
    assert Post.objects.count() == 1
    assert post.user == user
    assert post.body is not None
    assert post.created_at is not None
