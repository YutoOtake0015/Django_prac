from django.urls import path
from .views import hellofunc, HelloClass

urlpatterns = [
    path('hello/', hellofunc),
    path('hello2/', HelloClass.as_view()),
]