  
from django.db import models
#
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    def _create_User(self, email, password, is_staff, is_superuser, is_active, **extra_fields):
        User = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        User.set_password(password)
        User.save(using=self.db)
        return User
    
    # def create_user(self, email, password=None, **extra_fields):
    #     return self._create_User(email, password, True, False, True, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_User(email, password, True, True, True, **extra_fields)