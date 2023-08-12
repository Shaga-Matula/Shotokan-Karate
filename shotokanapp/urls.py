from .import views
from django.urls import path
from django.views.generic.base import TemplateView
from .forms import KyuRegisterForm
from .views import StudentListView 


urlpatterns = [
    path('', views.FirstPage.as_view(), name="home"),
    path('success/', TemplateView.as_view(template_name="success.html"), name='success'),
    path('addkyu/', views.KyuRegisterView.as_view(), name='kyuregister'),
    path('student_list/', views.StudentListView.as_view(), name='studentlist'),
    path('edit_record/<int:pk>', views.UpdateStudentView.as_view(), name='edit_record'),
    path('delete_record/<int:pk>', views.DeleteStudentView.as_view(), name='delete_record'),
    path('student_view/<int:pk>', views.StudentPageView.as_view(), name='students_page'),
    path('kyu_list', views.KyuListView.as_view(), name='kyu_list'),
    path('edit_kyu_list/<int:pk>', views.UpdateKyuView.as_view(), name='edit_kyu_list'),
    path('delete_kyu/<int:pk>', views.DeleteKyuView.as_view(), name='delete_kyu'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('student_page/', views.StudentPageView.as_view(), name ='student_page'),

]