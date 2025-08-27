# apps/budgets/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.expenses.models import Expense
from .models import Budget
from django.db.models import Sum

def update_budget_spent(user, year, month):
    budget = Budget.objects.filter(user=user, year=year, month=month).first()
    if budget:
        total_spent = (
            Expense.objects.filter(user=user, date__year=year, date__month=month)
            .aggregate(total=Sum("amount"))["total"] or 0
        )
        budget.spent = total_spent
        budget.save(update_fields=["spent"])

@receiver(post_save, sender=Expense)
def expense_saved(sender, instance, **kwargs):
    update_budget_spent(instance.user, instance.date.year, instance.date.month)

@receiver(post_delete, sender=Expense)
def expense_deleted(sender, instance, **kwargs):
    update_budget_spent(instance.user, instance.date.year, instance.date.month)
