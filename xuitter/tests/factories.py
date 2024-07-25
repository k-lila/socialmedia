import factory
from django.contrib.auth.models import User
from xuitter.models import Profile, Post


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "teste123")

    class Meta:
        model = User
        skip_postgeneration_save = True


class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    profile_bio = factory.Faker("text", max_nb_chars=300)
    profile_website = factory.Faker("url")

    class Meta:
        model = Profile


class PostFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    body = factory.Faker("text", max_nb_chars=140)

    class Meta:
        model = Post
