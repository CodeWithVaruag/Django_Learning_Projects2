from django.contrib.auth.models import BaseUserManager
from django.db import models

class userManager(BaseUserManager):
    def create_user(self,email, password=None,username=None,phone=None,**extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email =self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def super_user(self,email, password=None,username=None,phone=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password,username,**extra_fields)
        
