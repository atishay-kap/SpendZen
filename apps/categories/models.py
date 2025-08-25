from django.db import models
from django.conf import settings
from apps.common.base import BaseModel

# Create your models here.

class Category(BaseModel):
    
    name = models.CharField(max_length=100 , unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="If null, this is a global category"
    )
    
    def __str__(self):
        return self.name