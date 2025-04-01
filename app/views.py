from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем пользователя
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})
