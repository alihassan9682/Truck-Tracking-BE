from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import User_manager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    objects = User_manager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    def __str__(self):
        return self.email

class Profile(models.Model):
    linked_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    USER_TYPES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=USER_TYPES,default='user', blank=False)
    user_id = models.CharField(max_length=20,unique = True)
    email = models.EmailField(blank=False, null=False, unique =True)
    fname = models.CharField(max_length=20, blank=False, null=False)
    lname = models.CharField(max_length=20, blank=False, null=False)
    number = models.IntegerField(null=True, blank=True)
    photo = models.TextField(null=True, blank=True)
    REQUIRED_FIELDS = ['user_id','email','fname','lname']
    def __str__(self):
        return self.email
    