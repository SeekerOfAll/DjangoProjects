from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import UserRegistrationForm


class SignInView(LoginView):
    template_name = 'blog/login.html'


class LogoutView(LogoutView):
    template_name = 'blog/login.html'
    # redirect_field_name = 'login/'


class SignUpView(CreateView):
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm
