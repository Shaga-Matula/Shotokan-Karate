from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField



# These are the Models for my Karate School Database 


# This Model is for Karate Grade Information 

class StudentLevelMod(models.Model):
    kyu_level = models.CharField(max_length=15, verbose_name='Kyu Level')
    belt_color = models.CharField(max_length=50, verbose_name='Karate Belt Color')
    kata_name = models.CharField(max_length=50, verbose_name='Kata Name')
    kata_image = CloudinaryField('image', default='placeholder')
    syllabus_image = CloudinaryField('image', default='placeholder')

    class Meta:
        verbose_name = "Kyu Level"
        verbose_name_plural = "Kyu Levels"
        ordering = ["-kyu_level"]

    def __str__(self):
        return self.kyu_level


class SenseiMod(models.Model):
    sensei_first_name = models.CharField(max_length=50, verbose_name='Sensei Name')
    sensei_last_name = models.CharField(max_length=50, verbose_name='Sensei Last Name')
    sensei_email = models.EmailField(verbose_name='Sensei Email Address')
    sensei_contact_num = PhoneNumberField(verbose_name='Sensei Mobile')


    class Meta:
        verbose_name = "Sensei"
        verbose_name_plural = "Sensei"
        ordering = ["-sensei_first_name"]

    def __str__(self):
        return self.sensei_first_name



class CustomUser(AbstractUser):

    readonly_fields = ('last_updated',)
    # Custom User Model
    class Meta:
        verbose_name = "Shotokan Members"
        verbose_name_plural = "Shotokan Members"

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
    contact_num = PhoneNumberField(verbose_name='Student Contact Number', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Last Update')
    post_code = models.CharField(max_length=10, verbose_name='Post Code')
    email = models.EmailField(verbose_name='Email Address')

    student_grade = models.ForeignKey(StudentLevelMod, on_delete=models.PROTECT, default=1, verbose_name='Kyu To Achieve')
    sensei = models.ForeignKey(SenseiMod, on_delete=models.PROTECT, default=None, verbose_name='Sensei', null=True)
    
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


# This is the contact model for index.html form

class Contact(models.Model):
    
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    fname = models.CharField(max_length=50, verbose_name='First Name')
    lname = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.EmailField(verbose_name='Email Address')
    phone = models.CharField(max_length=20, verbose_name='Contact Number')
    msg = models.TextField(verbose_name='Message')
    level = models.CharField(max_length=20, verbose_name='Level')

def __str__(self):
        return f"{self.lname}, {self.fname}"