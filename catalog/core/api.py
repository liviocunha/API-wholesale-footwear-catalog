from django.shortcuts import get_object_or_404
from typing import List
from ninja import Router
from ninja.security import django_auth, APIKeyQuery
from .models import Client, Category
from .schemas import ClientIn, ClientOut, CategoryIn, CategoryOut
from .utils import generate_api_key, str_upper, str_title


class ApiKey(APIKeyQuery):
    param_name = "api_key"

    def authenticate(self, request, key):
        try:
            return Client.objects.get(key=key)
        except Client.DoesNotExist:
            pass


router = Router()
api_key = ApiKey()


@router.post("/client", auth=django_auth, tags=["generate client api Key"])
def create_client(request, payload: ClientIn):
    new_key = False
    while not new_key:
        key = generate_api_key()
        try:
            get_client = Client.objects.get(key=key)
        except Client.DoesNotExist:
            new_key = True

    client = Client.objects.create(key=key, **payload.dict())
    return {"id": client.id, "client": client.client, "api_key": client.key}


@router.get("/client", response=List[ClientOut], auth=django_auth, tags=["generate client api Key"])
def list_client(request):
    qs = Client.objects.all()
    return qs


@router.post("/category", auth=api_key, tags=["category"])
def create_category(request, payload: CategoryIn):
    data = payload.dict()
    client = Client.objects.get(key=request.auth.key)
    try:
        categories = Category.objects.filter(client=client)
        get_category = categories.get(title=str_upper(data['title']))
        return {"detail": f"The {str_title(data['title'])} category already exists, please insert a new one."}
    except Category.DoesNotExist:

        category = Category.objects.create(client=client, title=str_upper(data['title']))
        return {"id": category.id, "title": category.title.title()}


@router.get("/category/{title}", response=CategoryOut, auth=api_key, tags=["category"])
def get_category(request, title: str):
    title = str_upper(title)
    try:
        client = Client.objects.get(key=request.auth.key)
        categories = Category.objects.filter(client=client)
        category_one = categories.get(title=str_upper(title))
        print(type(category_one))
        print(category_one)
        return category_one
    except Category.DoesNotExist:
        return {'id': None, 'client': None, 'title': None, 'detail': 'No categories for this client'}
