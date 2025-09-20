from django.db import models
from apps.common.base import BaseModel
from django.conf import settings

class Budget(BaseModel):
    MONTH_CHOICES = [
        (1, "January"), (2, "February"), (3, "March"),
        (4, "April"), (5, "May"), (6, "June"),
        (7, "July"), (8, "August"), (9, "September"),
        (10, "October"), (11, "November"), (12, "December"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    month = models.IntegerField(choices=MONTH_CHOICES)
    year = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        unique_together = ("user", "month", "year")
            
    @property
    def spent(self):
        from apps.expenses.models import Expense
        total = Expense.objects.filter(
            user=self.user,
            date__year=self.year,
            date__month=self.month,
        ).aggregate(models.Sum("amount"))["amount__sum"] or 0
        return total
    
    @property
    def remaining(self):
        return self.amount - self.spent
    
    @property
    def overspent(self):
        return self.spent > self.amount