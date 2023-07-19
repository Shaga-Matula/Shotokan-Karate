from django.views.generic import View
from django.shortcuts import render
from .models import StudentInfoMod
from .forms import StudentForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic.base import TemplateView

# Create your views here.

class firstpage(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context)


from django.urls import reverse


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