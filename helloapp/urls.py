from django.urls import path
from .views import hellofunc

urlpatterns = [
    path('', hellofunc),
]