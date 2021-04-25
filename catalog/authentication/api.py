import datetime

import jwt
import pytz as pytz
from django.conf import settings
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from ninja import Router
from ninja.security import HttpBearer

from .forms import CustomUserCreationForm, AuthForm, PasswordResetForm
from .models import CustomUser, UserToken, AccessTypeModel
from .schemas import RegisterSchema, UserAuthSchema, ErrorMessage, LoginSchema, \
    AccessTokenSchema, MailConfirmedSchema, ResetPasswordResponseSchema, ResetPasswordSchema

router = Router()

secret = settings.SECRET_KEY
from_email_system = settings.DEFAULT_FROM_EMAIL


class TokenAuth(HttpBearer):
    def authenticate(self, request, key):
        try:
            data = jwt.decode(key, secret, algorithms="HS256")
            request.user_id = data['sub']
            user_token = UserToken.objects.get(user_id=request.user_id)
            if key != user_token.active_access_token:
                return None
        except jwt.PyJWTError:
            return None

        return data


@router.post('/retailer/register', response={200: UserAuthSchema, 400: ErrorMessage})
def retailer_register(request, payload: RegisterSchema):
    form = CustomUserCreationForm(payload.dict())
    is_valid = form.is_valid()

    if is_valid:
        user = form.save()
        user.refresh_from_db()
        user.is_active = False
        user.access_type = AccessTypeModel.objects.get(id=3)
        user.save()
        if not user.is_active:
            created_user = CustomUser.objects.get(pk=user.id)
            access_token = _generate_access_token(created_user)
            activation_link = f'http://127.0.0.1:8000/api/authentication/activate/{access_token}'
            send_mail('Activation Mail', f'Click to activate. {activation_link}', from_email_system, [user.email],
                      fail_silently=False, )
        return 200, user
    else:
        return 400, {"errors": form.error_messages}


@router.get('/activate/{token}', response={201: MailConfirmedSchema, 400: ErrorMessage})
def activate(request, token: str):
    decoded = jwt.decode(token, secret, algorithms="HS256")
    user_id = decoded['sub']
    user = CustomUser.objects.get(pk=user_id)
    user.is_active = True
    user.save()
    return 201, {"result": "activated"}


@router.post('/login', response={200: AccessTokenSchema, 401: ErrorMessage})
def login(request, payload: LoginSchema):
    form = AuthForm(request, payload.dict())
    is_valid = form.is_valid()
    if is_valid:
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)
        if user:

            access_token = _generate_access_token(user)
            user_token = None
            try:
                user_token = UserToken.objects.get(user=user)
            except:
                pass
            if user_token is None:
                UserToken.objects.create(user=user, active_access_token=access_token)
            else:
                user_token.active_access_token = access_token
                user_token.save()
            user.save()  # to check online count. It triggers last_logged_in
            return 200, {"access_token": access_token}
        else:
            return 401, {"errors": {"Invalid_credentials": "Credentials are not found"}}
    else:
        return 401, {"errors": form.error_messages}


@router.post('/reset-password', response={200: ResetPasswordResponseSchema, 400: ErrorMessage})
def reset_password(request, payload: ResetPasswordSchema):
    reset_form = PasswordResetForm(payload.dict())
    if reset_form.is_valid():
        reset_form.save(from_email=from_email_system, request=request)
        return 200, {'result': 'Reset password has been sent.'}
    else:
        return 400, {'errors': {'Password reset error': 'The provided information is invalid.'}}


def _generate_access_token(user: CustomUser):
    now = datetime.datetime.now(tz=pytz.utc)
    payload = {
        "sub": user.id,
        "iss": user.email,
        "iat": now
    }

    payload.update({"exp": now + datetime.timedelta(minutes=10)})
    access_token = jwt.encode(payload, secret, algorithm="HS256")
    return access_token