""" Imported modules: """
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, DetailView, DeleteView
from django.views.generic.edit import FormView, UpdateView
from .forms import StudentForm, KyuRegisterForm, StudentForm, CustomUserCreationForm, SenseiRegisterForm
from .models import StudentLevelMod, CustomUser, SenseiMod
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin


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

class StudentKyuListView(TemplateView):
    """
    This view is for displaying a list of students based on their kyu level.

    Attributes:
        template_name: The name of the template to use
        for the view, which is 'student_kyu_list.html'.
    """
    
    template_name = 'student_kyu_list.html'

    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for the view.

        Returns:
        A dictionary containing the context data.
        """
        context = super().get_context_data(**kwargs)
        user_kyu_level = self.request.user.student_grade.kyu_level
        records = StudentLevelMod.objects.filter(kyu_level__gte=user_kyu_level)
        context['student'] = records

        return context


#########################################################
#############      Kyu Class Functions   ################


class DeleteKyuView(DeleteView):
    """
    A view for deleting a Student Record in
    `StudentLevelMod` object.   
    """
    model = StudentLevelMod
    form_class = StudentForm
    template_name = 'delete_kyu.html'
    success_url = reverse_lazy('success')


class KyuListView(TemplateView):
    template_name = 'kyu_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kyu_list'] = StudentLevelMod.objects.all()
        return context


class KyuRegisterView(FormView):
    template_name = 'kyu_regester.html'
    form_class = KyuRegisterForm
    success_url = 'success.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('success')


class UpdateKyuView(UpdateView):
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
#########################################


class UpdateSenseiView(UpdateView):
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


class SenseiRegisterView(FormView):
    template_name = 'reg_sensei.html'
    form_class = SenseiRegisterForm
    success_url = 'success.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('success')


class SenseiListView(TemplateView):
    template_name = 'sensei_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sensei_list'] = SenseiMod.objects.all()
        return context


class DeleteSenseiView(DeleteView):
    model = SenseiMod
    form_class = SenseiListView
    template_name = 'delete_sensei.html'
    success_url = reverse_lazy('success')


#########################################################
#############       Custom User      ####################

class RegisterView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.role == 'TEACHER'

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        return render(request, 'register.html', {'form': form})


class StudentListView(TemplateView):
    template_name = 'student_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = CustomUser.objects.all()
        return context


class UpdateStudentView(UpdateView):
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


class DeleteStudentView(DeleteView):
    model = CustomUser
    form_class = StudentForm
    template_name = 'delete_record.html'
    success_url = reverse_lazy('success')
