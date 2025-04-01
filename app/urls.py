from django.urls import path
from .views import register, IndexView, ProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),  # URL для регистрации
    path('', IndexView.as_view(), name='index'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html', next_page='profile'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
