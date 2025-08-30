from django.urls import path
from .views import dashboard_view, expenses_by_category, expenses_by_month, daily_cumulative_expenses

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("expenses-by-category/", expenses_by_category, name="expenses_by_category"),
    path("expenses-by-month/", expenses_by_month, name="expenses_by_month"),
    path("daily-cumulative/", daily_cumulative_expenses, name="daily_cumulative_expenses"),
]
