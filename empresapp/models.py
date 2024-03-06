from django import forms
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser,UserManager 
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    id= models.IntegerField(primary_key=True)
    username = models.EmailField(_('email address'), unique=True,null=False,blank=True) 
    password = models.CharField(max_length=250)
    display_name = models.CharField(max_length=250,null=False,blank=False)
    first_name = models.CharField(max_length=250,blank=True)
    last_name = models.CharField(max_length=250,blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password','is_superuser','is_active','date_joined']

    GENRE_CHOICES = [(False,'Hombre'),(True,'Mujer'),(None,'Otro')]
    address = models.CharField(max_length=250,null=True,verbose_name="Dirección")
    Genre = models.BooleanField(null=False,default=True)

    class Meta:
        db_table="MyUsers"
        ordering = ['id']

    def create_superuser(self,username,email,password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.email + " " + str(self.first_name) + " " + str(self.last_name)