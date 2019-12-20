from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
# Create your models here.


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            return ValueError("must have email")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


"""
    AbstractUser: 
    Use this option if you are happy with the existing fields on the User model and just want to 
    remove the username field.
    AbstractBaseUser: 
    Use this option if you want to start from scratch by creating your own,completely new User model.
"""


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return "@{}".format(self.name)
