from django import forms
from .models import StudentInfoMod, StudentLevelMod


# from django.forms import ModelForm
# from .models import StudentLevelMod

# class PhotoForm(ModelForm):
#     class Meta:
#         model = StudentLevelMod
#         fields = ['kata_image', 'syllabus_image']


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentInfoMod
        fields = [
            'first_name',
            'last_name',
            'email',
            'address_1',
            'address_2',
            'date_of_birth',
            'post_code',
            'student_grade',
        ]


class KyuRegisterForm(forms.ModelForm):
    class Meta:
        model = StudentLevelMod
        fields = [
            'kyu_level',
            'belt_color',
            'kata_name',
            'kata_image',
            'syllabus_image',
        ]


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = StudentInfoMod
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'email',
            'address_1',
            'address_2',
            'post_code',
            'student_grade',
        ]
