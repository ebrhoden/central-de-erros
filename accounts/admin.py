from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = 'email',
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    ordering = 'email',


admin.site.register(Account, AccountAdmin)
