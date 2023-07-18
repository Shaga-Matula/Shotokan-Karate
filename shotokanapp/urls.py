from .import views
from django.urls import path



urlpatterns = [
    path('', views.firstpage.as_view(), name="home"),
    
]