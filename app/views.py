from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView
from django.db import IntegrityError


class IndexView(TemplateView):
    template_name = 'app\index.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'app\profile.html'
    login_url = reverse_lazy('login')  # используется для указания URL-адреса, если пользователь не аутентифицирован


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('login')
            except IntegrityError:
                form.add_error('username', 'Пользователь с таким именем уже существует.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})

