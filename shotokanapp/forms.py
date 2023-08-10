from django import forms
from .models import StudentInfoMod, StudentLevelMod, CustomUser
from django.contrib.auth.forms import UserCreationForm


# from django.forms import ModelForm
# from .models import StudentLevelMod

# class PhotoForm(ModelForm):
#     class Meta:
#         model = StudentLevelMod
#         fields = ['kata_image', 'syllabus_image']


class user_sign_up(forms.ModelForm):
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
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'address_1',
            'address_2',
            'post_code',
            'student_grade',
        ]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('address_1', 'address_2', 'date_of_birth', 'post_code', 'first_name', 'last_name', 'student_grade','email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.address_1 = self.cleaned_data['address_1']
        user.address_2 = self.cleaned_data['address_2']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.post_code = self.cleaned_data['post_code']
        user.student_grade = self.cleaned_data['student_grade']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
