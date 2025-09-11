from django.contrib import admin
from .models import Budget

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ("user", "month", "year", "amount", "remaining")
    list_filter = ("year", "month", "user")
    search_fields = ("user__username",)
