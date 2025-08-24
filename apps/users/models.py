from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.common.base import BaseModel
# Create your models here.

class User(AbstractUser, BaseModel):
    
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username