from django.urls import path
from . import views

app_name = "analytics"

urlpatterns = [
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("data/category/", views.expenses_by_category, name="expenses_by_category"),
    path("data/monthly/", views.expenses_by_month, name="expenses_by_month"),
]