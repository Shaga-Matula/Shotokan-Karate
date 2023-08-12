from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser, Group, Permission


# These are the Models for my Karate School Database 


# This Model is for Karate Grade Information 

class StudentLevelMod(models.Model):
    kyu_level = models.CharField(max_length=15, verbose_name='Kyu Level')
    belt_color = models.CharField(max_length=50, verbose_name='Karate Belt Color')
    kata_name = models.CharField(max_length=50, verbose_name='Kata Name')
    kata_image = CloudinaryField('image', default='placeholder')
    syllabus_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-kyu_level"]

    def __str__(self):
        return self.kyu_level


class CustomUser(AbstractUser):
    # Custom User Model
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        STUDENT = 'STUDENT', 'Student'
        TEACHER = 'TEACHER', 'Teacher'
        
    base_role = Role.STUDENT
    
    role = models.CharField(max_length=15, choices=Role.choices, default=base_role)
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    address_1 = models.CharField(max_length=50, verbose_name='Address Line One')
    address_2 = models.CharField(max_length=50, verbose_name='Address Line Two', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Date of Birth', null=True, blank=True)
    post_code = models.CharField(max_length=10, verbose_name='Post Code')
    email = models.EmailField(verbose_name='Email Address')
    student_grade = models.ForeignKey(StudentLevelMod, on_delete=models.PROTECT, default=1, verbose_name='Student grade')
    
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username
