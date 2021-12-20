from django.views.generic import (
    FormView, View
)
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls.base import reverse_lazy, reverse
#
from .models import User
from .forms import UserRegisterForm, LoginForm


class UserRegisterFormView(FormView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('user_app:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            # **extra_fields
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero']
        )

        return super(UserRegisterFormView, self).form_valid(form)


class LoginUserView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('book_app:list-book')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)

        return super(LoginUserView, self).form_valid(form)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'user_app:login'
            )
        )