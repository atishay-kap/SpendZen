from django.db import models
from apps.common.base import BaseModel
from django.conf import settings

class Budget(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    month = models.IntegerField()
    year = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    spent = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = ("user", "month", "year")

    @property
    def remaining(self):
        return self.amount - self.spent
