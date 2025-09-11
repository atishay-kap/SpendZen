from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.expenses.models import Expense
from .models import Budget

def update_budget(budget):
    """
    Recalculate and update the spent value for a given budget.
    """
    total = (
        Expense.objects.filter(
            user=budget.user,
            date__year=budget.year,
            date__month=budget.month,
        ).aggregate(total=Sum("amount"))["total"] or 0
    )
    budget.spent = total
    budget.save(update_fields=["spent"])


@receiver([post_save, post_delete], sender=Expense)
def handle_expense_change(sender, instance, **kwargs):
    """
    Whenever an Expense is created, updated, or deleted:
    - If a Budget exists for that user/month/year → update it.
    - If not → create one with amount=0 and spent = actual total.
    """
    budget, created = Budget.objects.get_or_create(
        user=instance.user,
        year=instance.date.year,
        month=instance.date.month,
        defaults={"amount": 0, "spent": 0},
    )

    update_budget(budget)
