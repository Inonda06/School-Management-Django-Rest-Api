from django.db import models

from email.mime import image
from pickle import FALSE
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class UserProfile(models.Model):
    LEVELS = (
        (1, 'Level One'),
        (2, 'Level Two'),

    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    preferred_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    discord_name = models.CharField(max_length=100)
    codeopen_name = models.CharField(max_length=100)
    github_username = models.CharField(max_length=100)
    current_level = models.IntegerField(choices=LEVELS)
    fcc_profile_url = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
