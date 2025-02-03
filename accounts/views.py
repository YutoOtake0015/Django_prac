from django.contrib import messages 
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm

# Create your views here.
class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('index')
    
    def form_invalid(self, form):
        print(form.errors)  # どんなエラーが発生しているか確認
        messages.error(self.request, "入力に誤りがあります。")
        return super().form_invalid(form)