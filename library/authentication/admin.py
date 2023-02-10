from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'middle_name', 'email', 'created_at', 'updated_at', 'role',
                    'is_active', 'is_staff', 'is_superuser')
    # list_filter = ('id', 'first_name', 'last_name', 'middle_name', 'email', 'created_at', 'updated_at', 'role',
    #                'is_active', 'is_staff', 'is_superuser')


admin.site.register(CustomUser, CustomUserAdmin)
