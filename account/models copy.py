from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random


class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    roles= (
        ('admin', 'admin'),
        ('author', 'author'),
        ('reader', 'reader'),
      )
    id = models.AutoField(primary_key=True, null=False, blank=False, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='photos/userPhoto', blank=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=30, choices=roles)
    phone_number = models.CharField(max_length=50)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.username}'

    def get_email(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    
    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                self.id = random.randint(1000, 99999)
                if not Account.objects.filter(id=self.id).exists():
                    break
        super().save(*args, **kwargs)

