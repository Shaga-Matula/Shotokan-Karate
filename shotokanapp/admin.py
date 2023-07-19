from django.contrib import admin

# Register your models here.

from .models import StudentInfoMod, StudentLevelMod

admin.site.register(StudentInfoMod)
admin.site.register(StudentLevelMod)