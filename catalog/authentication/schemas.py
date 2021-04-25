from typing import Any, Dict

from ninja import Schema
from ninja.orm import create_schema
from catalog.authentication import models

UserAuthSchema = create_schema(models.CustomUser,
                               fields=['id', 'email', 'first_name', 'last_name'])

UserProfileSchema = create_schema(models.CustomUser,
                                  fields=['email', 'first_name', 'last_name', 'phone'])

EditProfileResponseSchema = create_schema(models.CustomUser,
                                          fields=['email', 'first_name', 'last_name', 'phone'])


class AccessTokenSchema(Schema):
    access_token: str


class ErrorMessage(Schema):
    errors: Dict[str, Any]


class MailConfirmedSchema(Schema):
    result: str


class LoginSchema(Schema):
    username: str
    password: str


class RegisterSchema(Schema):
    email: str
    first_name: str
    last_name: str
    phone: int
    password1: str
    password2: str


class PasswordSchema(Schema):
    result: Dict[str, Any]


class ResetPasswordSchema(Schema):
    email: str


class ResetPasswordResponseSchema(Schema):
    result: str