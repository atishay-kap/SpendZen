from django.db import models
from django.conf import settings
from apps.common.base import BaseModel
from apps.categories.models import Category

# Create your models here.

class Expense(BaseModel):
    
    PAYMENT_CHOICES = [
        ('CASH','Cash'),
        ('CARD','Card'),
        ('UPI','UPI'),
        ('OTHER','Other'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category , on_delete=models.SET_NULL , null=True , blank=True)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    description = models.TextField(blank=True , null=True)
    date = models.DateField()
    payment_method = models.CharField(max_length=10 , choices=PAYMENT_CHOICES , default='CASH')
    
    def __str__(self):
        return f"{self.user.username} - {self.amount} ({self.category})"
    