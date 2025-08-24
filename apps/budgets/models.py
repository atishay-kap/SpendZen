from django.db import models
from django.conf import settings
from apps.common.base import BaseModel

# Create your models here.

class Budget(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    spent = models.DecimalField(max_digits=10 , decimal_places=2 , default=0.00)
    
    def __str__(self):
        return f"{self.user.username} - {self.month} budget"
    