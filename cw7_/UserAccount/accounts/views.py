from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomLoginView(LoginView):
    template_name = 'custom_auth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    template_name = 'custom_auth/logout.html'


class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('profile')
    template_name = 'custom_auth/signup.html'


class CustomUserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'custom_auth/profile.html'
    permission_required = 'auth.view_user'


class CustomUserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'custom_auth/edit_profile.html'
    permission_required = 'auth.change_user'
