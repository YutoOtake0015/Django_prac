from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def hellofunc(request):
    return HttpResponse('hello')

class HelloClass(TemplateView):
    template_name  = 'hello2.html'
