from django.contrib import admin
from .models import StudentLevelMod, CustomUser
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, StudentForm
from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import CustomUser

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User





admin.site.unregister(SocialApp)
admin.site.unregister(Group)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)



class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (None, {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'address_1', 'address_2', 'post_code')}),
        (None, {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'date_of_birth', 'address_1', 'address_2', 'post_code', 'role'),
        }),
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(StudentLevelMod)
