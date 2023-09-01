""" Imported modules: """
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, DetailView, DeleteView
from django.views.generic.edit import FormView, UpdateView
from .forms import KyuRegisterForm, StudentForm, CustomUserCreationForm
from .forms import SenseiRegisterForm
from .models import StudentLevelMod, CustomUser, SenseiMod
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        level = request.POST.get('chk1')
        contact = Contact(fname=fname, lname=lname, email=email, phone=phone, msg=msg, level=level)
        contact.save()
        return render(request, 'success.html')
    return render(request, 'index.html')


#################################################
class FirstPage(View):
    """
    This FirstPage class is used to handle the landing page request
    and display the information in a FormView.
    """

    def get(self, request, *args, **kwargs):
        context = {'username': request.user.username, }
        return render(request, 'index.html', context)


########################################################
###############   Student Classs Functions #############

class StudentKyuListView(UserPassesTestMixin, TemplateView):
    """
    This view: Displays a list of students based on their 
    next atainable kyu level.

    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'STUDENT'
        return False

    template_name = 'student_kyu_list.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user_kyu_level = self.request.user.student_grade.kyu_level
        records = StudentLevelMod.objects.filter(kyu_level__gte=user_kyu_level)
        context['student'] = records

        return context


#########################################################
#############      Kyu Class Functions   ################


class DeleteKyuView(UserPassesTestMixin, DeleteView):
    """
    This view: Instructors with the Teacher 
    Role to displayDisplays a Belt View with the 
    ability to delete it.

    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'TEACHER'
        return False

    model = StudentLevelMod
    form_class = StudentForm
    template_name = 'delete_kyu.html'
    success_url = reverse_lazy('success')


class KyuListView(UserPassesTestMixin, TemplateView):
    """
    This view: Allows Instructors with the Teacher 
    Role to display a list of all the Belt Levels or 
    kyu level.

    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'TEACHER'
        return False

    template_name = 'kyu_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kyu_list'] = StudentLevelMod.objects.all()
        return context


class KyuRegisterView(UserPassesTestMixin, FormView):
    """
    This view: Enables the Instructors with the Teacher 
    Role to Create New Kyu's or Belt Levels.

    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'TEACHER'
        return False

    template_name = 'kyu_regester.html'
    form_class = KyuRegisterForm
    success_url = 'success.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('success')


class UpdateKyuView(UserPassesTestMixin, UpdateView):
    """
    This view: Allows the Instructors with the Teacher role 
    update the kyu records.

    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'TEACHER'
        return False

    model = StudentLevelMod
    form_class = KyuRegisterForm
    template_name = 'edit_kyu.html'
    success_url = reverse_lazy('success')

    def get_object(self, queryset=None):
        obj = get_object_or_404(StudentLevelMod, pk=self.kwargs['pk'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('success')


#########################################################
#############      Sensei Views      ####################


class UpdateSenseiView(UserPassesTestMixin, UpdateView):
    """
    This view: Allows the Instructors with the Teacher role 
    update Sensei records.

    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'TEACHER'
        return False

    model = SenseiMod
    form_class = SenseiRegisterForm
    template_name = 'edit_sensei.html'
    success_url = reverse_lazy('success')

    def get_object(self, queryset=None):
        obj = get_object_or_404(SenseiMod, pk=self.kwargs['pk'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('success')


class SenseiRegisterView(UserPassesTestMixin, FormView):
    """
    This view: Allows the Instructors with the Teacher role 
    register new sensei.

    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'TEACHER'
        return False

    template_name = 'reg_sensei.html'
    form_class = SenseiRegisterForm
    success_url = 'success.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('success')


class SenseiListView(UserPassesTestMixin, TemplateView):
    """
    This view: Allows the Instructors with the Teacher role 
    view a list of senseis'.

    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'TEACHER'
        return False

    template_name = 'sensei_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sensei_list'] = SenseiMod.objects.all()
        return context


class DeleteSenseiView(UserPassesTestMixin, DeleteView):
    """
    This view: Allows the Instructors with the Teacher role 
    delete a Sensei record.

    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'TEACHER'
        return False

    model = SenseiMod
    form_class = SenseiListView
    template_name = 'delete_sensei.html'
    success_url = reverse_lazy('success')


#########################################################
#############       Custom User      ####################


class RegisterView(UserPassesTestMixin, View):
    """ 
    This view: Allows the Instructors with the Teacher role 
    to register new users and assign roles, sensei and grades. 
    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'TEACHER'
        return False

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        return render(request, 'register.html', {'form': form})


class StudentListView(UserPassesTestMixin, TemplateView):
    """ 
    This view: Allows the Instructors with the Teacher role 
    to view a list of students.
    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'TEACHER'
        return False

    template_name = 'student_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = CustomUser.objects.all()
        return context


class UpdateStudentView(UserPassesTestMixin, UpdateView):
    """ 
    This view: Allows the Instructors with the Teacher role 
    to edit a student record.
    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'TEACHER'
        return False

    model = CustomUser
    form_class = StudentForm
    template_name = 'edit_record.html'
    success_url = reverse_lazy('success')

    def get_object(self, queryset=None):
        obj = get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('success')


class DeleteStudentView(UserPassesTestMixin, DeleteView):
    """ 
    This view: Allows the Instructors with the Teacher role 
    delete a student record.
    """

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.role == 'TEACHER'
        return False

    model = CustomUser
    form_class = StudentForm
    template_name = 'delete_record.html'
    success_url = reverse_lazy('success')
