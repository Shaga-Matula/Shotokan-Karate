from django.contrib import admin
from .models import StudentInfoMod, StudentLevelMod, CustomUser
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp

admin.site.register(StudentInfoMod)
admin.site.register(StudentLevelMod)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, UpdateStudentForm
from .models import CustomUser

### Custom Admin Model


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form =  UpdateStudentForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)