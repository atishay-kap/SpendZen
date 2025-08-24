from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'category', 'payment_method', 'date', 'created_at')
    list_filter = ('category', 'payment_method', 'date')
    search_fields = ('description',)
    ordering = ('-date',)
