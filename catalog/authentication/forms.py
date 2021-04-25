from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm as _PasswordResetForm, \
    SetPasswordForm as _SetPasswordForm
from django import forms

from .models import CustomUser


class AuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'input is-medium', 'placeholder': 'E-mail'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'input is-medium', 'placeholder': 'Senha'}
        )
    )


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'

        self.fields['email'].label = 'E-mail'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'

        self.fields['first_name'].label = 'Nome'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nome'

        self.fields['last_name'].label = 'Sobrenome'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Sobrenome'

        self.fields['phone'].label = 'Telefone'
        self.fields['phone'].widget.attrs['placeholder'] = 'Telefone'

        self.fields['password1'].label = 'Senha'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'

        self.fields['password2'].label = 'Confirmação de senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmação de senha'

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone')


class PasswordResetForm(_PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'input is-medium', 'placeholder': 'E-mail'})
    )


class SetPasswordForm(_SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'input is-medium', 'placeholder': 'Nova Senha'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'input is-medium', 'placeholder': 'Confirmação de senha'}),
    )