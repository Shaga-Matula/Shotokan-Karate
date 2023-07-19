from .import views
from django.urls import path
from django.views.generic.base import TemplateView



urlpatterns = [
    path('', views.firstpage.as_view(), name="home"),
    path('addstudent/', views.StudentRegesterView.as_view(), name='StudentRegister'),
    path('success/', TemplateView.as_view(template_name="success.html"), name='success')
]