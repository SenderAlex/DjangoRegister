from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'app\index.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'app\profile.html'
    login_url = reverse_lazy('login')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем пользователя
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})
