from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'

from django.shortcuts import render

def about(request):
    return render(request, 'about.html')
