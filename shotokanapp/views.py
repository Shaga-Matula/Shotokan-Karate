from django.views.generic import View
from django.shortcuts import render

# Create your views here.

class firstpage(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context)