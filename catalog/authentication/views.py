from django.contrib.auth.views import PasswordResetView as _PasswordResetView, \
    PasswordResetConfirmView as _PasswordResetConfirmView

from x.forms import PasswordResetForm, SetPasswordForm


class PasswordResetView(_PasswordResetView):
    form_class = PasswordResetForm


class PasswordResetConfirmView(_PasswordResetConfirmView):
    reset_url_token = 'create-a-password'
    form_class = SetPasswordForm