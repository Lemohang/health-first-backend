from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile

# Customize User admin
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Role & Extra Info", {"fields": ("is_patient", "is_provider", "location")}),
    )
    list_display = ("username", "email", "is_patient", "is_provider", "location", "is_staff")
    list_filter = ("is_patient", "is_provider", "is_staff")
    search_fields = ("username", "email", "location")

# Profile inline for quick edit from User page
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]

# Register models
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
