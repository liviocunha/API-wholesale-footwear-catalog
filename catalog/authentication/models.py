from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class AccessTypeModel(models.Model):
    type = models.CharField(max_length=50)

    @classmethod
    def create_type_profile(cls, **kwargs):
        return cls.objects.create(**kwargs)
    
    def __str__(self):
        return f'{self.type}'


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    last_logged_in = models.DateTimeField(auto_now=True)
    access_type = models.ForeignKey(to=AccessTypeModel,on_delete=models.DO_NOTHING,related_name='profile', default=2)
    create_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=25)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    @property
    def full_name(self):
        return self.get_full_name()

    def __str__(self):
        return f'{self.access_type} | {self.first_name} {self.last_name} ({self.email})'


class UserToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    active_access_token = models.CharField(_('active_access_token'), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}'
