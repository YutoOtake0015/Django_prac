from django.contrib import admin
from django.urls import path
from .views import hellofunc, HelloClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hellofunc),
    path("hello2/", HelloClass.as_view()),
]
