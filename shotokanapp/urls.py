from .import views
from django.urls import path
from django.views.generic.base import TemplateView
from .forms import KyuRegisterForm
from .views import StudentListView, StudentKyuListView,SenseiRegisterView


urlpatterns = [
    ###################   Home/Success Page #######################

    path('', views.FirstPage.as_view(), name='home'),
    path('success/', TemplateView.as_view(template_name="success.html"), name='success'),
 
    
    ###################   Student CRUD    ##########################
    
    path('register/', views.RegisterView.as_view(), name='register'),
    path('student_list/', views.StudentListView.as_view(), name='studentlist'),
    path('edit_record/<int:pk>', views.UpdateStudentView.as_view(), name='edit_record'),
    path('delete_record/<int:pk>', views.DeleteStudentView.as_view(), name='delete_record'),
    
    ###################   Kyu CRUD    ##############################
    
    path('addkyu/', views.KyuRegisterView.as_view(), name='kyuregister'),
    path('kyu_list', views.KyuListView.as_view(), name='kyu_list'),
    path('edit_kyu_list/<int:pk>', views.UpdateKyuView.as_view(), name='edit_kyu_list'),
    path('delete_kyu/<int:pk>', views.DeleteKyuView.as_view(), name='delete_kyu'),
    
    ##################   Sensei CRUD   ############################
    path('create_sensei/', views.SenseiRegisterView.as_view(), name='create_sensei'),
    path('sensei_list/', views.SenseiListView.as_view(), name='sensei_list'),
    path('edit_sensei/<int:pk>', views.UpdateSenseiView.as_view(), name='edit_sensei'),
    path('delete_sensei/<int:pk>', views.DeleteSenseiView.as_view(), name='delete_sensei'),

    ###################   Student Syllabus  ########################
    
    path('student_kyu_list/', views.StudentKyuListView.as_view(), name= 'student_kyu_list'),

]