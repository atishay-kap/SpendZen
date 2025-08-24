from django.contrib import admin
from .models import Budget

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'month', 'amount', 'spent', 'created_at', 'updated_at')
    list_filter = ('month', 'user')
    search_fields = ('user__email',)
    ordering = ('-month',)
