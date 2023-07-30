""" Imported modules: """
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, DetailView, DeleteView
from django.views.generic.edit import FormView, UpdateView
from .forms import StudentForm, KyuRegisterForm, UpdateStudentForm
from .models import StudentInfoMod, StudentLevelMod


class FirstPage(View):
    def get(self, request, *args, **kwargs):
        context = {'username': request.user.username, }
        return render(request, 'index.html', context)


class StudentRegesterView(FormView):
    """ A view for registering a new student. """

    template_name = 'student_regester.html'
    form_class = StudentForm
    success_url = 'success.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('success')


class KyuRegisterView(FormView):
    template_name = 'kyu_regester.html'
    form_class = KyuRegisterForm
    success_url = 'success.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('success')

class KyuListView(TemplateView):
    template_name = 'kyu_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kyu_list'] = StudentLevelMod.objects.all()
        return context


class StudentListView(TemplateView):
    template_name = 'student_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = StudentInfoMod.objects.all()
        return context


class StudentPageView(TemplateView):
    template_name = 'student_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_page'] = StudentLevelMod.objects.all()
        return context


class UpdateStudentView(UpdateView):
    model = StudentInfoMod
    form_class = UpdateStudentForm
    template_name = 'edit_record.html'
    success_url = reverse_lazy('success')

    def get_object(self, queryset=None):
        obj = get_object_or_404(StudentInfoMod, pk=self.kwargs['pk'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('success')


class DeleteStudentView(DeleteView):
    model = StudentInfoMod
    form_class = UpdateStudentForm
    template_name = 'delete_record.html'
    success_url = reverse_lazy('success')


class DeleteKyuView(DeleteView):
    model = StudentLevelMod
    form_class = UpdateStudentForm
    template_name = 'delete_kyu.html'
    success_url = reverse_lazy('success')


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
