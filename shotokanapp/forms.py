from django import forms
from .models import StudentLevelMod, CustomUser, SenseiMod
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SenseiRegisterForm(forms.ModelForm):
    class Meta:
        model = SenseiMod
        fields = [
            'sensei_first_name',
            'sensei_last_name',
            'sensei_email',
            'sensei_contact_num',
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


class StudentForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'address_1',
            'address_2',
            'post_code',
            'email',
            'role',
            'student_grade',
            'sensei',
        ]


class CustomUserCreationForm(UserCreationForm):
    helper = FormHelper()
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'register'))

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
                                                 'role', 'first_name',
                                                 'last_name', 'address_1',
                                                 'address_2', 'student_grade',
                                                 'sensei', 'post_code',
                                                 'email', 'date_of_birth',
                                                 'contact_num', 
                                                 'student_grade',
                                                 'sensei', 'role')
        
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'},
                                             format='%d/%m/%Y'),
        }
        input_formats = ['%d/%m/%Y']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.address_1 = self.cleaned_data['address_1']
        user.address_2 = self.cleaned_data['address_2']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.post_code = self.cleaned_data['post_code']
        user.contact_num = self.cleaned_data['contact_num']
        user.role = self.cleaned_data.get('role')
        user.student_grade = self.cleaned_data['student_grade']
        user.email = self.cleaned_data['email']
        user.sensei_first_name = self.cleaned_data['sensei']

        if commit:
            user.save()
        return user