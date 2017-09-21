from blog.models import Post
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
from random import randint


class Command(BaseCommand):
    help = 'Seeds the database with mock data.'

    def __init__(self):
        super().__init__()

    def add_arguments(self, parser):
        pass

    def random_post(self):
        return Post(
            title='Alpha{}'.format(randint(10000, 99999)),
            created_at=timezone.now(),
            updated_at=timezone.now(),
            author='Scott Greenup',
            content='# Heading\nWords go here.'
        )

    def save_user(self, user):
        """
        Saves the user to the database; either by creating a new user, or by
        updating the user with the same username.
        """

        def print_user(writer, user, action):
            role = "user"

            if user.is_staff:
                role = "staff"

            if user.is_superuser:
                role = "superuser"

            writer.write(
                "{action} {role}: {username} <{email}>"
                .format(
                    action=action,
                    role=role,
                    username=user.username,
                    email=user.email))

        try:
            u = User.objects.get(username=user.username)
            u.username = user.username
            u.set_password(user.password)
            u.email = user.username
            u.is_staff = user.is_staff
            u.is_superuser = user.is_superuser
            u.save()
            print_user(self.stdout, user, "Updated")

        except Exception:
            user = User.objects.create_user(
                username=user.username,
                password=user.password,
                email=user.email,
                is_staff=user.is_staff,
                is_superuser=user.is_superuser)
            print_user(self.stdout, user, "Created")

    def handle(self, *args, **options):
        """This is the entry point for this management command."""

        users = [User(
            username='sg',
            email='scott.j.greenup@gmail.com',
            password='qwerqwer1234',
            is_staff=True,
            is_superuser=True)]

        for user in users:
            self.save_user(user)

        for i in range(0, 10):
            post = self.random_post()
            post.save()
