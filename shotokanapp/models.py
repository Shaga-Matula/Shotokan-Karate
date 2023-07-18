from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# These are the Models for my Karate School Database 



    # This Model is for Karate Grade Information 

class StudentLevelMod(models.Model):
    kyu_level = models.CharField(max_length=10, verbose_name='Kyu Level')
    belt_color = models.CharField(max_length=50, verbose_name='Karate Belt Color')
    kata_name = models.CharField(max_length=50, verbose_name='Kata Name')
    kata_image = CloudinaryField('image', default='placeholder')
    syllabus_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-kyu_level"]

    def __str__(self):
        return self.kyu_level


#  This Model is for Karate Students Information

class StudentInfoMod(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    email = models.EmailField(verbose_name='Email Address')
    address_1 = models.CharField(max_length=50, verbose_name='Address Line One')
    address_2 = models.CharField(max_length=50, verbose_name='Address Line Two', blank=True, null=True)
    post_code = models.CharField(max_length=10, verbose_name='Post Code')
    updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')
    student_grade = models.ForeignKey(StudentLevelMod, on_delete=models.CASCADE, default=9, verbose_name='Student Grade')

    class Meta:
        ordering = ["id"]  # Built in "ID PK" will be used for Student_ID

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


