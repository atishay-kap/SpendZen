from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.expenses.models import Expense
from .models import Budget

def update_budget(budget):
    total = Expense.objects.filter(
        user=budget.user,
        date__year=budget.year,
        date__month=budget.month,
    ).aggregate(total=Sum("amount"))["total"] or 0
    budget.spent = total
    budget.save(update_fields=["spent"])

@receiver(post_save, sender=Expense)
@receiver(post_delete, sender=Expense)
def handle_expense_change(sender, instance, **kwargs):
    try:
        budget = Budget.objects.get(
            user=instance.user,
            year=instance.date.year,
            month=instance.date.month,
        )
        update_budget(budget)
    except Budget.DoesNotExist:
        Budget.objects.create(
            user=instance.user, 
            year=instance.date.year, 
            month=instance.date.month, 
            amount=0, 
            spent=instance.amount
            )
