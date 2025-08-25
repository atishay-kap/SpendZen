import random
from datetime import timedelta, date
from django.contrib.auth import get_user_model
from apps.expenses.models import Expense, Category

User = get_user_model()

def seed_expenses():
    user = User.objects.first()
    if not user:
        print("❌ No user found. Create one first.")
        return

    categories = list(Category.objects.all())
    if not categories:
        print("❌ No categories found. Run seed_categories first.")
        return

    payment_methods = ["CASH", "CARD", "UPI", "OTHER"]

    for i in range(30):
        Expense.objects.create(
            user=user,
            category=random.choice(categories),
            amount=random.randint(100, 5000),
            description=f"Test expense {i+1}",
            date=date.today() - timedelta(days=random.randint(0, 30)),
            payment_method=random.choice(payment_methods),
        )

    print("✅ Expenses seeded successfully!")
