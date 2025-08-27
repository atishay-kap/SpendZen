from django.db import models
from django.conf import settings
from apps.common.base import BaseModel
from apps.expenses.models import Expense
from django.db.models import Sum
import datetime

class Budget(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    month = models.PositiveIntegerField()  # 1–12
    year = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        unique_together = ("user", "month", "year")

    def __str__(self):
        return f"{self.user.username} - {self.month}/{self.year} Budget"

    @property
    def remaining(self):
        return self.amount - self.spent
