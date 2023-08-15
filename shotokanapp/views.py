""" Imported modules: """
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, DetailView, DeleteView
from django.views.generic.edit import FormView, UpdateView
from .forms import StudentForm, KyuRegisterForm, StudentForm, CustomUserCreationForm
from .models import StudentLevelMod, CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View


class FirstPage(View):
    """
    This FirstPage class is used to handle the landing page request and display the
    information in a FormView. The get() method is called when someone visits
    the page, and it takes in a request object that contains information
    about the request made by the user. Inside the get() method, the variable called
    context is created to store the username of the user making the request and
    display the username on screen when loged in along with the page 'index.html'.
    """

    def get(self, request, *args, **kwargs):
        context = {'username': request.user.username, }
        return render(request, 'index.html', context)


########################################################
###############   Student Page View   ##################


# class StudentPageView(TemplateView):
#     template_name = 'student_page.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['student_page'] = StudentLevelMod.objects.all()
#         return context


class StudentKyuListView(TemplateView):
    template_name = 'student_kyu_list.html'

       
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_kyu_level = self.request.user.student_grade.kyu_level
        records = StudentLevelMod.objects.filter(kyu_level__gte=user_kyu_level)
        context['student'] = records
   
        return context



#########################################################
#############      Kyu Table views    ###################

################    Kyu Create    #######################


class KyuRegisterView(FormView):
    template_name = 'kyu_regester.html'
    form_class = KyuRegisterForm
    success_url = 'success.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('success')


##############       Kyu Read       #######################


class KyuListView(TemplateView):
    template_name = 'kyu_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kyu_list'] = StudentLevelMod.objects.all()
        return context


##############     Kyu Update       #######################


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


#################    Kyu Delete    ########################


class DeleteKyuView(DeleteView):
    model = StudentLevelMod
    form_class = StudentForm
    template_name = 'delete_kyu.html'
    success_url = reverse_lazy('success')


#########################################################
#############       Custom User      ####################


##############       User Create    ######################


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        return render(request, 'register.html', {'form': form})

##############      User Read     ######################

class StudentListView(TemplateView):
    template_name = 'student_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = CustomUser.objects.all()
        return context

##############      User Update     ######################

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

##############      User Delete     ######################

class DeleteStudentView(DeleteView):
    model = CustomUser
    form_class = StudentForm
    template_name = 'delete_record.html'
    success_url = reverse_lazy('success')









