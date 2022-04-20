
from django.contrib import admin
from .models import UserProfile, User
from django.contrib.auth.admin import UserAdmin as BaseUser

@admin.register(User)
class BaseAdminUser(BaseUser):
    list_display = ('email', 'is_student', 'is_staff', 'is_admin',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('permissions', {'fields': ('is_admin', 'is_staff', 'is_student')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('email', 'password1', 'passwords2'),
        })
    )
    ordering = ('email',)
    filter_horizontal = ()
    search_fields = ('email',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass






