from .import views
from django.urls import path
from django.views.generic.base import TemplateView
from .forms import KyuRegisterForm


urlpatterns = [
    path('', views.firstpage.as_view(), name="home"),
    path('addstudent/', views.StudentRegesterView.as_view(), name='StudentRegister'),
    path('success/', TemplateView.as_view(template_name="success.html"), name='success'),
    path('addkyu/', views.KyuRegisterView.as_view(), name='kyuregister'),
    path('student_list/', views.StudentListView.as_view(), name='studentlist'),
    path('edit_record/<int:pk>', views.UpdateStudentView.as_view(), name='edit_record'),
    path('delete_record/<int:pk>', views.DeleteStudentView.as_view(), name='delete_record'),
    # path('student_view/<int:pk>', views.StudentPageView.as_view(), name='students_page'),

]