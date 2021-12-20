from django import forms
from django.contrib.auth import authenticate

from . models import User


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese su contraseña...',
                'class': 'form-control',
                'style': '{  }'
            }
        )
    )
    password2 = forms.CharField(
        label='Repetir contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir contraseña...',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'nombres', 'apellidos', 'genero')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

    # validation for the passwords
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden')


class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese su nombre de usuario...',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label='contrasena',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese su contraseña',
                'class': 'form-control'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos del usuario no son correctos')
        return self.cleaned_data
