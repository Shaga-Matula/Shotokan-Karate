from .import views
from django.urls import path



urlpatterns = [
    path('', views.firstpage.as_view(), name="home"),
    path('addstudent/', views.StudentRegesterView.as_view(), name='StudentRegister'),
    path('success/', views.StudentRegesterView.as_view(), name='success'),
]