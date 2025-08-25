from apps.expenses.models import Category

def seed_categories():
    categories = [
        "Food", "Transport", "Bills", "Entertainment",
        "Shopping", "Health", "Travel", "Education", "Other"
    ]
    for name in categories:
        Category.objects.get_or_create(name=name)
    print("✅ Categories seeded successfully!")
