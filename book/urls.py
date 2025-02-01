
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.ListBookView.as_view(), name='list-book'),
    path("book_detail/<int:pk>", views.DetailBookView.as_view(), name='detail-book'),
    path("book/create/", views.CreateBookView.as_view(), name='create-book'),
    path("book/delete/<int:pk>", views.DeleteBookView.as_view(), name='delete-view'),
]
