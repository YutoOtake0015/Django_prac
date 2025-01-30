
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.ListBookView.as_view()),
    path("book_detail/<int:pk>", views.DetailBookView.as_view())
]
