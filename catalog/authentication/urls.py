from django.urls import path

from .views import PasswordResetConfirmView

urlpatterns = [
    path('activate/<token>'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]