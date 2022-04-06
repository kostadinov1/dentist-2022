from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import admin as auth_admin, get_user_model

from dentist_3_project.accounts.forms import UserRegistrationForm, UserChangeAdminForm
from dentist_3_project.accounts.models import AppUser, Profile

CustomUserModel = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = UserChangeAdminForm
    model = CustomUserModel
    list_display = ('email', 'is_staff', 'is_active','is_superuser'  )
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUserModel, CustomUserAdmin)

# @admin.register(AppUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'is_staff', 'is_superuser', 'date_joined')
#     # form = UserChangeAdminForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
    # list_display = ('first_name', 'last_name', 'phone', 'dob', 'gender')

