from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_superuser(self, email, username, password, **of):
        of.setdefault( 'is_staff', True)
        of.setdefault( 'is_superuser', True)
        return self.create_user(email, username, password, **of)

    def create_user(self, email, username, password, **of):
        user = self.model(email=email, username=username, **of)
        user.set_password(password)
        user.save()
        return user


class InventoryUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, blank=False, unique=True)
    email = models.EmailField(max_length=200, blank=False, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_owner = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']