from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email','access_type')
    list_filter = ('email','access_type','last_logged_in','create_date')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'phone','access_type', 'active')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'access_type',
             'create_date', 'active', 'last_logged_in')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)