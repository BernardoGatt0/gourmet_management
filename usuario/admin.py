from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from usuario import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username', 'name']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            ('Informações Pessoais'),
            {'fields': ('name', 'date')}
        ),
        (
            ('Permissões'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),

    )


admin.site.register(models.User, UserAdmin)
