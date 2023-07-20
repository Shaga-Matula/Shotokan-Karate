from django.views.generic import View
from django.shortcuts import render
from .models import StudentInfoMod
from .forms import StudentForm, KyuRegisterForm, UpdateStudentForm
from django.views.generic.edit import FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView


# Create your views here.

class firstpage(View):
    def get(self, request, *args, **kwargs):
        context = {
            'username': request.user.username,
        }
        return render(request, 'index.html', context)


class StudentRegesterView(FormView):
    template_name = 'student_regester.html'
    form_class = StudentForm
    success_url = 'success.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('success')

    # def get(self, request, *args, **kwargs):
    #     return render(request, 'success.html')


class KyuRegisterView(FormView):
    template_name = 'kyu_regester.html'
    form_class = KyuRegisterForm
    success_url = 'success.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('success')


class StudentListView(TemplateView):
    template_name = 'student_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = StudentInfoMod.objects.all()
        return context

class UpdateStudentView(UpdateView):
    model = StudentInfoMod
    template_name = 'edit_record.html'
    form_class = UpdateStudentForm
    success_url = reverse_lazy('success')

    # def get_object(self, queryset=None):
    #     obj = get_object_or_404(self.model, Student_ID=self.kwargs['Student_ID'])
    #     return obj

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)