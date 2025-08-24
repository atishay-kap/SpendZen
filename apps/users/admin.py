from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'email', 'username', 'is_staff', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('-created_at',)

    # Make timestamps read-only
    readonly_fields = ('created_at', 'updated_at')