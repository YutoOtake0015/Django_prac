from django.http import HttpResponse
from django.views.generic import TemplateView


def hellofunc(request):
    responseobject = HttpResponse('hello world')
    return responseobject

class HelloClass(TemplateView):
    template_name = 'hello2.html'
