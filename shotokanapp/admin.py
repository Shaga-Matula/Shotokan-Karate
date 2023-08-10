from django.contrib import admin

# Register your models here.

from .models import StudentInfoMod, StudentLevelMod, CustomUser

admin.site.register(StudentInfoMod)
admin.site.register(StudentLevelMod)
admin.site.register(CustomUser)