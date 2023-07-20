from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from .models import StudentInfoMod
from .forms import StudentForm, KyuRegisterForm, UpdateStudentForm
from django.views.generic.edit import FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

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
    form_class = UpdateStudentForm
    template_name = 'edit_record.html'
    success_url = reverse_lazy('success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('edit_record', kwargs={'pk': self.object.pk})

    # def get_object(self, queryset=None):
    #     id_ = self.kwargs.get('id')
    #     try:
    #         return get_object_or_404(StudentInfoMod, pk=id_)
    #     except StudentInfoMod.DoesNotExist:
    #         raise Http404('Does Not Exist')


# class UpdateStudentView(UpdateView):
#     model = StudentInfoMod
#     template_name = 'edit_record.html'
#     form_class = UpdateStudentForm
#     success_url = reverse_lazy('success')

#     def get_object(self, queryset=None):
#         id_ = self.kwargs.get('id')
#         try:
#             return get_object_or_404(StudentInfoMod, pk=id_)
#         except StudentInfoMod.DoesNotExist:
#             raise Http404('Does Not Exist')

# class UpdateStudentView(UpdateView):
#     model = StudentInfoMod
#     template_name = 'edit_record.html'
#     form_class = UpdateStudentForm
#     success_url = reverse_lazy('success')

#     def get_object(self, queryset=None):
#         id_ = self.kwargs.get('id')
#         try:
#             return get_object_or_404(StudentInfoMod, id=id_)
#         except StudentInfoMod.DoesNotExist:
#             raise Http404('Does Not Exist')

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     obj = self.get_object()
#     #     context['student_id'] = obj
#     #     return context


# class UpdateStudentView(UpdateView):
#     model = StudentInfoMod
#     template_name = 'edit_record.html'
#     form_class = UpdateStudentForm
#     success_url = reverse_lazy('success')

#     def get_object(self, queryset=None):
#         id_ = self.kwargs.get('id')
#         return get_object_or_404(StudentInfoMod, id=id_)

#     def form_valid(self, form):
#         self.object = form.save()
#         return super().form_valid(form)


# class UpdateStudentView(UpdateView):
#     model = StudentInfoMod
#     template_name = 'edit_record.html'
#     form_class = UpdateStudentForm
#     success_url = reverse_lazy('success')

#     def get_object(self, queryset=None):
#         id_ = self.kwargs.get('id')
#         try:
#             return get_object_or_404(StudentInfoMod, pk=id_)
#         except StudentInfoMod.DoesNotExist:
#             raise Http404('Does Not Exist')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         obj = self.get_object()
#         context['student_id'] = obj
#         return context
