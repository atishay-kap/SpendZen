from django.db import models
from apps.common.base import BaseModel

# Create your models here.

class Category(BaseModel):
    
    name = models.CharField(max_length=100 , unique=True)
    
    def __str__(self):
        return self.name