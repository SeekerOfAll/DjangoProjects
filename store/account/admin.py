from django.contrib import admin
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.utils.translation import ugettext_lazy as _

from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'is_staff']
    change_password_form = AdminPasswordChangeForm
    ordering = ('email',)
    add_fieldsets = ((None, {
        'classes': ('wide',),
        'fields': ('email', 'full_name', 'password1', 'password2')
    }),
                     )
    fieldsets = ((_('authentication'), {
        "fields": ('email', 'password',)
    }),
                 (_('personal info'), {
                     "fields": ('full_name', 'avatar')
                 }),
                 (_('Permission'), {
                     "fields": ('is_staff', 'is_active', 'is_superuser',)
                 }),
                 (_('Important dates'), {
                     "fields": ('last_login',)
                 }),
                 )


# Register your models here.
admin.site.register(User, UserAdmin)
