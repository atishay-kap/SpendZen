from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from apps.budgets.models import Budget
from apps.expenses.models import Expense, Category

User = get_user_model()

class BudgetSignalTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="pass")
        self.category = Category.objects.create(name="Food")

    def create_budget(self, month=None, year=None, amount=1000):
        today = timezone.now().date()
        return Budget.objects.create(
            user=self.user,
            month=month or today.month,
            year=year or today.year,
            amount=amount,
        )

    def test_expense_create_updates_budget(self):
        budget = self.create_budget(amount=1000)
        Expense.objects.create(
            user=self.user,
            category=self.category,
            amount=200,
            date=timezone.now().date(),
        )
        budget.refresh_from_db()
        self.assertEqual(budget.spent, 200)
        self.assertEqual(budget.remaining, 800)

    def test_expense_update_recalculates_budget(self):
        budget = self.create_budget(amount=1000)
        exp = Expense.objects.create(
            user=self.user,
            category=self.category,
            amount=200,
            date=timezone.now().date(),
        )
        exp.amount = 500
        exp.save()
        budget.refresh_from_db()
        self.assertEqual(budget.spent, 500)
        self.assertEqual(budget.remaining, 500)

    def test_expense_delete_updates_budget(self):
        budget = self.create_budget(amount=1000)
        exp = Expense.objects.create(
            user=self.user,
            category=self.category,
            amount=200,
            date=timezone.now().date(),
        )
        exp.delete()
        budget.refresh_from_db()
        self.assertEqual(budget.spent, 0)
        self.assertEqual(budget.remaining, 1000)

    def test_multiple_expenses_accumulate(self):
        budget = self.create_budget(amount=1000)
        Expense.objects.create(user=self.user, category=self.category, amount=200, date=timezone.now().date())
        Expense.objects.create(user=self.user, category=self.category, amount=300, date=timezone.now().date())
        budget.refresh_from_db()
        self.assertEqual(budget.spent, 500)
        self.assertEqual(budget.remaining, 500)

    def test_expense_in_other_month_does_not_affect(self):
        today = timezone.now().date()
        budget = self.create_budget(month=today.month, year=today.year, amount=1000)
        # Expense in different month
        other_date = today.replace(month=(today.month % 12) + 1)
        Expense.objects.create(user=self.user, category=self.category, amount=300, date=other_date)
        budget.refresh_from_db()
        self.assertEqual(budget.spent, 0)
        self.assertEqual(budget.remaining, 1000)
