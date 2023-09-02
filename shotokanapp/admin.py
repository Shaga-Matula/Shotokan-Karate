from .models import StudentLevelMod, CustomUser, SenseiMod, Contact
from allauth.socialaccount.models import SocialToken, SocialAccount
from allauth.socialaccount.models import SocialApp, EmailAddress
from .forms import CustomUserCreationForm, StudentForm
from django.contrib import admin, sites
from django.contrib.auth.admin import UserAdmin, Group
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


admin.site.unregister(SocialApp)
admin.site.unregister(Group)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
admin.site.unregister(EmailAddress)
admin.site.unregister(Site)

admin.site.register(StudentLevelMod)
admin.site.register(SenseiMod)
admin.site.register(Contact)

# This id for the User Contact in index.html


class CustomContactAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('fname', 'lname', 'email', 'phone', 'msg',
                           'level')}),
    )
    list_display = ('fname', 'lname', 'email', 'phone', 'msg', 'level')
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('fname', 'lname', 'email', 'phone', 'msg', 'level'),
                }),
    )

    def __str__(self):
        return f"{self.fname} {self.lname}"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (None, {'fields': ('first_name', 'last_name', 'email', 'date_of_birth',
         'address_1', 'address_2', 'post_code', 'contact_num')}),
        (None, {'fields': ('role', 'student_grade', 'sensei',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'role', 'student_grade', 'sensei', 'contact_num', 'last_updated')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name',
                       'last_name', 'email', 'date_of_birth', 'address_1', 'address_2',
                       'post_code', 'contact_num', 'role', 'student_grade', 'sensei'),
        }),
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
